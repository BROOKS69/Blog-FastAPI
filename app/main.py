from fastapi import FastAPI, Depends
#from fastapi import status, Response, HTTPException
from blog import schemas, models, hashing
from blog.database import engine, get_db
#from sqlalchemy.orm import Session
#from typing import List
#from passlib.context import CryptContext
#from .hashing import Hash
from blog.routers import authentication, blog, user

# Create the database tables
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include routers for different functionalities
app.include_router(authentication.router)
app.include_router(blog.router)   
app.include_router(user.router) 



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)