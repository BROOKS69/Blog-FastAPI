from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import os
import logging

logger = logging.getLogger(__name__)

# MongoDB URL with better defaults for different environments
MONGODB_URL = os.getenv("MONGODB_URL")

# For local development fallback
if not MONGODB_URL:
    MONGODB_URL = "mongodb+srv://topboybrooks1_db_user:MoTaeY3DerWMPvG4@fastapidb.58pqx7t.mongodb.net/?retryWrites=true&w=majority&appName=FastAPIdb"

# Connection pool settings for serverless
client = AsyncIOMotorClient(
    MONGODB_URL,
    maxPoolSize=10,
    minPoolSize=1,
    maxIdleTimeMS=30000,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
    socketTimeoutMS=5000,
    waitQueueTimeoutMS=5000,
)

database = client.blogdb  # Use 'blogdb' as the database name

async def init_db():
    """Initialize database with proper error handling for serverless environments"""
    try:
        # Test the connection
        await client.admin.command('ping')
        logger.info("Successfully connected to MongoDB")

        # Import models here to avoid circular imports
        from . import models
        await init_beanie(database=database, document_models=[models.User, models.Blog])
        logger.info("Database initialized successfully with Beanie")

    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        logger.error("This might be due to:")
        logger.error("1. Missing MONGODB_URL environment variable")
        logger.error("2. Incorrect MongoDB connection string")
        logger.error("3. Network connectivity issues")
        logger.error("4. MongoDB server not running or accessible")
        logger.info("Continuing without database initialization - this may cause runtime errors")
        # Don't raise the exception to allow the app to start
        # But log it clearly so developers know there's an issue

def get_db():
    """Get database instance"""
    return database

async def close_db():
    """Close database connection"""
    try:
        client.close()
        logger.info("Database connection closed")
    except Exception as e:
        logger.error(f"Error closing database connection: {e}")
