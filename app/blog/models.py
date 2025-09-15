from beanie import Document, Link
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


class User(Document):
    name: str
    email: EmailStr
    password: str
    blogs: Optional[List[Link["Blog"]]] = []

    class Settings:
        name = "users"


class Blog(Document):
    title: str
    body: str
    creator: Link[User]

    class Settings:
        name = "blogs"
