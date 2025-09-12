from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from blog import schemas, models, database
from blog.hashing import Hash


# Initialize password context for hashing
def create(request: schemas.User, db: Session):
    hashed_password = Hash().bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
# Get a user
def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"User with id {id} is not found")
    return user         