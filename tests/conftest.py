import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import os
from app.blog import models
from app.main import app
from httpx import AsyncClient

@pytest.fixture(scope="session")
async def test_db():
    """Create a test database connection."""
    test_mongo_url = os.getenv("TEST_MONGODB_URL", "mongodb://localhost:27017/test_blogdb")
    client = AsyncIOMotorClient(test_mongo_url)
    test_database = client.get_database("test_blogdb")

    # Initialize Beanie with test models
    await init_beanie(database=test_database, document_models=[models.User, models.Blog])

    yield test_database

    # Cleanup: drop test database
    await client.drop_database("test_blogdb")
    client.close()

@pytest.fixture
async def client(test_db):
    """Create an async test client."""
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        yield ac

@pytest.fixture
async def test_user(test_db):
    """Create a test user."""
    user = models.User(name="Test User", email="test@example.com", password="hashedpassword")
    await user.insert()
    yield user
    await user.delete()

@pytest.fixture
async def auth_headers(client, test_user):
    """Get authentication headers for test user."""
    # First, we need to create a login endpoint test or mock JWT
    # For simplicity, we'll create a test token
    from app.blog.JWTtoken import create_access_token
    token = create_access_token(data={"sub": test_user.email})
    return {"Authorization": f"Bearer {token}"}
