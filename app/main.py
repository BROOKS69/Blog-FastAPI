import logging
import sys
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
import time

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from blog.database import init_db, close_db
from blog.routers import authentication, blog, user

# Configure logging for serverless environments
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global variable to track database initialization status
db_initialized = False

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for serverless environments"""
    global db_initialized

    logger.info("Starting Blog-FastAPI application...")
    logger.info(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")
    logger.info(f"Debug mode: {os.getenv('DEBUG', 'False')}")

    # Startup
    try:
        await init_db()
        db_initialized = True
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        db_initialized = False
        logger.error(f"❌ Failed to initialize database: {e}")
        logger.warning("⚠️  Application will start without database - API calls may fail")

    yield

    # Shutdown
    logger.info("Shutting down Blog-FastAPI application...")
    try:
        await close_db()
        logger.info("✅ Database connection closed successfully")
    except Exception as e:
        logger.error(f"❌ Error closing database connection: {e}")

# Create FastAPI app with better configuration
app = FastAPI(
    title="Blog-FastAPI",
    description="A FastAPI blog application with MongoDB",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
try:
    app.include_router(authentication.router)
    app.include_router(blog.router)
    app.include_router(user.router)
    logger.info("✅ All routers included successfully")
except Exception as e:
    logger.error(f"❌ Failed to include routers: {e}")
    raise

@app.get('/', tags=["ROOT"])
async def root():
    """Root endpoint with health check information"""
    return {
        "message": "Welcome to the Blog-FastAPI",
        "status": "running",
        "database": "connected" if db_initialized else "disconnected",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "timestamp": time.time()
    }

@app.get('/health', tags=["HEALTH"])
async def health_check():
    """Health check endpoint for serverless environments"""
    db_status = "healthy" if db_initialized else "unhealthy"

    if not db_initialized:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "status": "unhealthy",
                "database": "disconnected",
                "message": "Database connection failed during startup"
            }
        )

    return {
        "status": "healthy",
        "database": db_status,
        "environment": os.getenv("ENVIRONMENT", "development"),
        "timestamp": time.time()
    }

# Error handlers for better debugging
@app.exception_handler(500)
async def internal_error_handler(request, exc):
    logger.error(f"Internal server error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": "An unexpected error occurred. Please check the logs for details."
        }
    )

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
