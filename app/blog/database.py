from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import os

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017/blogdb")

client = AsyncIOMotorClient(MONGODB_URL)
database = client.get_database()

async def init_db():
    # Import models here to avoid circular imports
    from . import models
    await init_beanie(database=database, document_models=[models.User, models.Blog])

def get_db():
    return database
