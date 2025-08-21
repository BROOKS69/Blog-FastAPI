from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, models, database
from passlib.context import CryptContext
from ..hashing import Hash
from ..repository import user


router = APIRouter()
get_db = database.get_db


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/user', response_model=schemas.ShowUser, tags=["USERS"])
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/user/{id}', response_model=schemas.ShowUser, tags=["USERS"])
def get_user(id: int, db: Session = Depends(get_db)):
   return user.show(id, db)                         