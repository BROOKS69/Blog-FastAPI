from fastapi import APIRouter, HTTPException, status
from blog import schemas, models, JWTtoken
from blog.hashing import Hash

router = APIRouter(
    tags=["AUTHENTICATION"],
)

@router.post('/login', response_model=schemas.Token)
async def login(request: schemas.Login):
    user = await models.User.find_one(models.User.email == request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    if not Hash().verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")
