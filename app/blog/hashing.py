from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashing class to handle password hashing and verification
class Hash():
    def bcrypt(self, password: str):
        return pwd_cxt.hash(password)

    # Verify the password
    def verify(self, plain_password, hashed_password):
        return pwd_cxt.verify(plain_password, hashed_password)