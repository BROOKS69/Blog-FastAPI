from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from blog import schemas, models, database, oauth2
from typing import List
from blog.repository import blog

# Initialize APIRouter
router = APIRouter(
    prefix="/blog",
)
get_db = database.get_db

# Get all blogs endpoint with authentication
@router.get('/', response_model=List[schemas.ShowBlog], tags=["BLOGS"])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

# Create a blog
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog, tags=["BLOGS"])
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db, current_user.id)

# Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["BLOGS"])
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

# Update a blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog, tags=["BLOGS"])
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.update(id, request, db)


# Get a blog
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, tags=["BLOGS"])
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return blog.show(id, response, db)

