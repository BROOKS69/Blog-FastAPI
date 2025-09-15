from fastapi import APIRouter, Depends, status, HTTPException, Response
from blog import schemas, models, oauth2
from typing import List
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
)

# Get all blogs endpoint with authentication
@router.get('/', response_model=List[schemas.ShowBlog], tags=["BLOGS"])
async def get_all(current_user: schemas.User = Depends(oauth2.get_current_user)):
    return await blog.get_all()

# Create a blog
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog, tags=["BLOGS"])
async def create(request: schemas.Blog, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return await blog.create(request, current_user.id)

# Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["BLOGS"])
async def destroy(id: str, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return await blog.destroy(id)

# Update a blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog, tags=["BLOGS"])
async def update(id: str, request: schemas.Blog, current_user: schemas.User = Depends(oauth2.get_current_user)):
   return await blog.update(id, request)

# Get a blog
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, tags=["BLOGS"])
async def show(id: str, response: Response):
    return await blog.show(id, response)

