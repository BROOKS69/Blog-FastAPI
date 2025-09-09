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
   pip install fastapi uvicorn sqlalchemy pymysql passlib
   ```
2. **Configure your database connection** in `blog/database.py`.
3. **Run the API server:**
   ```
   uvicorn main:app --reload
   ```
4. **Access the interactive docs:**  
   Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## Folder Structure

- `blog/routers/` — API route definitions (e.g., user routes)
- `blog/models.py` — SQLAlchemy models
- `blog/schemas.py` — Pydantic schemas
- `blog/database.py` — Database connection setup
- `blog/repository/` — Business logic for CRUD operations

## Notes

- You can manage your MySQL database with MySQL Workbench or switch to MongoDB
