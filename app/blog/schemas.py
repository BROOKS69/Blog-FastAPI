from pydantic import BaseModel
from typing import List, Optional

# Blog schema
class Blog(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True


# User schema
class User(BaseModel):
    name: str
    email: str
    password: str

class Config:
    from_attributes = True

# Display user with blogs
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List
    
class Config:
    from_attributes = True   

class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser

class Config:
    from_attributes = True     

# Authentication
class Login(BaseModel):
    username: str
    password: str
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    scopes: list[str] = []
