# FastAPI Blog API

This project is a **FastAPI-based RESTful API** for managing users and blog posts. It demonstrates how to build a backend service using FastAPI, SQLAlchemy (for MySQL), and password hashing for user authentication. The API supports user creation, retrieval, and can be extended for blog post management.

## Main Features

- **User Registration:** Create new users with secure password hashing.
- **User Retrieval:** Fetch user details by ID.
- **Database Integration:** Connects to a MySQL database (can be adapted for MongoDB).
- **Modular Structure:** Organized with routers, models, schemas, and repository patterns.
- **Extensible:** Easily add endpoints for blog posts, authentication, and more.

## Getting Started

1. **Install dependencies:**
   ```
   pip install fastapi uvicorn sqlalchemy pymysql passlib python-jose[cryptography]
   ```
2. **Configure your database connection** in `blog/database.py`.
3. **Set environment variables** for security:
   - `SECRET_KEY` for JWT token signing
   - `DATABASE_URL` for database connection string
4. **Run the API server:**
   ```
   uvicorn app.main:app --reload
   ```
5. **Access the interactive docs:**  
   Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## Folder Structure

- `blog/routers/` — API route definitions (e.g., user routes)
- `blog/models.py` — SQLAlchemy models
- `blog/schemas.py` — Pydantic schemas
- `blog/database.py` — Database connection setup
- `blog/repository/` — Business logic for CRUD operations

## Refactor and Improvements Summary

- Fixed bugs in repository functions (update, delete) with proper error handling.
- Corrected Pydantic schemas with proper Config nesting.
- Improved authentication flow: fixed login endpoint, proper JWT token creation and verification.
- Added user fetching in OAuth2 dependency for current user.
- Removed unsafe `drop_all` calls; recommend using Alembic for migrations.
- Moved secrets and database URL to environment variables for security.
- Added type hints and cleaned imports across modules.
- Added consistent authentication checks on protected endpoints.
- Added logging for better traceability.
- Fixed hardcoded user IDs and improved user association in blog creation.

## Notes

- You can manage your MySQL database with MySQL Workbench or switch to MongoDB.
- Use Alembic for database migrations instead of dropping and recreating tables.
- Ensure environment variables are set before running the application.
