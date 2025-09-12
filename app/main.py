import logging
from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import authentication, blog, user

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the database tables
# Warning: drop_all is unsafe for production, consider using Alembic migrations
# models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
logger.info("Database tables created or verified.")

# Initialize FastAPI app
app = FastAPI()

# Include routers for different functionalities
app.include_router(authentication.router)
app.include_router(blog.router)   
app.include_router(user.router)
logger.info("Routers included successfully.")




# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)