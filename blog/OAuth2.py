from fastapi import Depends, HTTPException, status
import JWTtoken
from fastapi.security import OAuth2PasswordBearer

# JWT token configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Function to get the current user from the JWT token
def get_current_user(token: str = Depends(JWTtoken.oauth2_scheme)):
   credentials_exception = HTTPException(
       status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )
    return token.verify_JWTtoken(token, credentials_exception)    