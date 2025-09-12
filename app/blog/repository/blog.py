from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session, joinedload
from blog import schemas, models, database

# Initialize password context for hashing
def get_all(db: Session):
    blogs = db.query(models.Blog).options(joinedload(models.Blog.creator)).all()
    return blogs

# Additional code for blog operations
def create(request: schemas.Blog, db: Session, user_id: int):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Delete a blog
def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

# Update a blog
def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Blog with id {id} is not found")
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return 'updated'

# Get a blog
def show(id: int, response: Response, db: Session):
    blog = db.query(models.Blog).options(joinedload(models.Blog.creator)).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Blog with id {id} is not found")
    return blog
