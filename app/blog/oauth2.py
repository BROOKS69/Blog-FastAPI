from fastapi import Depends, HTTPException, status
from blog import JWTtoken, schemas, models
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = JWTtoken.verify_JWTtoken(token, credentials_exception)
    user = await models.User.find_one(models.User.email == token_data.email)
    if user is None:
        raise credentials_exception
    return user
