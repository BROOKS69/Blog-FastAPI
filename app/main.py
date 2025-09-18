import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from blog.database import init_db
from blog.routers import authentication, blog, user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await init_db()
        logger.info("Database initialized.")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        logger.info("Continuing without database initialization.")
    yield

app = FastAPI(title="Blog-FastAPI", lifespan=lifespan)



app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
logger.info("Routers included successfully.")

@app.get('/' , tags=["ROOT"])
async def root():
    return {"message": "Welcome to the Blog-FastAPI"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)