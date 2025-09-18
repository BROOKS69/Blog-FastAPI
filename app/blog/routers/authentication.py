from fastapi import APIRouter, HTTPException, status
from blog import schemas, models, JWTtoken
from blog.hashing import Hash

router = APIRouter(
    tags=["AUTHENTICATION"],
)

@router.post('/register', response_model=schemas.ShowUser)
async def register(request: schemas.User):
    existing_user = await models.User.find_one(models.User.email == request.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    hashed_password = Hash().bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    await new_user.insert()
    return new_user

@router.post('/login', response_model=schemas.Token)
async def login(request: schemas.Login):
    user = await models.User.find_one(models.User.email == request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    if not Hash().verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")
