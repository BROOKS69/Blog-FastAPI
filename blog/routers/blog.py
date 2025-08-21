from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, models, database, OAuth2
from typing import List
from passlib.context import CryptContext
from ..repository import blog

router = APIRouter()
get_db = database.get_db
 
@router.get('/blog', response_model=List[schemas.ShowBlog], tags=["BLOGS"])
def get_all(db: Session = Depends(get_db), get_current_user: schemas.TokenData = Depends(JWTtoken.get_current_user)):
    #blogs = db.query(models.Blog).all()
    return blog.get_all(db)

@router.post('/blog', status_code=status.HTTP_201_CREATED, response_model=schemas.Blog, tags=["BLOGS"])
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog.create(request, db)
    return blog.create(request, db)

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["BLOGS"])
def destroy(id: int,  db: Session = Depends(get_db)):
    return blog.destroy(id, db)



@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["BLOGS"])
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
   return blog.update(id, request, db)


# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=["blogs"])
# def get_all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@router.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=["BLOGS"])
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return blog.show(id, response, db)


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/user', response_model=schemas.ShowUser, tags=["USERS"])
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    hashed_password = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/user/{id}', response_model=schemas.ShowUser, tags=["USERS"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"User with id {id} is not found")
    return user                                
