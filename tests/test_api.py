import pytest
from httpx import AsyncClient
from app.blog import models

@pytest.mark.asyncio
async def test_create_user(client):
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "password123"
    }
    response = await client.post("/user/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert "id" in data

@pytest.mark.asyncio
async def test_login(client, test_user):
    login_data = {
        "username": "test@example.com",
        "password": "hashedpassword"  # Note: in real test, hash the password
    }
    response = await client.post("/login", json=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_get_user(client, test_user):
    response = await client.get(f"/user/{test_user.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_user.name
    assert data["email"] == test_user.email

@pytest.mark.asyncio
async def test_create_blog(client, auth_headers, test_user):
    blog_data = {
        "title": "Test Blog",
        "body": "This is a test blog post."
    }
    response = await client.post("/blog/", json=blog_data, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == blog_data["title"]
    assert data["body"] == blog_data["body"]
    assert "id" in data

@pytest.mark.asyncio
async def test_get_blogs(client, auth_headers):
    response = await client.get("/blog/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.asyncio
async def test_get_blog(client, auth_headers):
    # First create a blog
    blog_data = {
        "title": "Another Test Blog",
        "body": "Content here."
    }
    create_response = await client.post("/blog/", json=blog_data, headers=auth_headers)
    blog_id = create_response.json()["id"]

    response = await client.get(f"/blog/{blog_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == blog_data["title"]
