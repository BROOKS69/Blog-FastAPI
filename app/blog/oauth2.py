from fastapi import Depends, HTTPException, status
from blog import JWTtoken, schemas, models, database
from fastapi.security import OAuth2PasswordBearer


# JWT token configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dependency to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return JWTtoken.verify_JWTtoken(token, credentials_exception)