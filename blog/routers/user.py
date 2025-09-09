from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, models, database
from passlib.context import CryptContext
from ..hashing import Hash
from ..repository import user

# Initialize APIRouter
router = APIRouter(
    prefix="/user",
)
get_db = database.get_db

# Additional code for user creation with password hashing
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/', response_model=schemas.ShowUser, tags=["USERS"])
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request, db)

# Get a user
@router.get('/', response_model=schemas.ShowUser, tags=["USERS"])
def get_user(id: int, db: Session = Depends(get_db)):
   return user.show(id, db)                         