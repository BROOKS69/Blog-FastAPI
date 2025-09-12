from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from blog import schemas, database, models, JWTtoken
from blog.hashing import Hash

# Initialize APIRouter
router = APIRouter(
    tags=["AUTHENTICATION"],
)

# Login endpoint
@router.post('/login', response_model=schemas.Token)
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    # Check if user exists
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    # Verify password
    if not Hash().verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")

    # Generate JWT token and return response
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")
