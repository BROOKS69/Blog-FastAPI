from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, models, database, oauth2
from typing import List
from passlib.context import CryptContext
from ..repository import blog

# Initialize APIRouter
router = APIRouter(
    prefix="/blog",
)
get_db = database.get_db
 
# Get all blogs endpoint with authentication
@router.get('/', response_model=List[schemas.ShowBlog], tags=["BLOGS"])
def get_all(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    #blogs = db.query(models.Blog).all()
    return blog.get_all(db)

# Create a blog
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Blog, tags=["BLOGS"])
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog.create(request, db)
    return blog.create(request, db)

# Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["BLOGS"])
def destroy(id: int,  db: Session = Depends(get_db)):
    return blog.destroy(id, db)


# Update a blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["BLOGS"])
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
   return blog.update(id, request, db)


# Get a blog
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, tags=["BLOGS"])
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return blog.show(id, response, db)

