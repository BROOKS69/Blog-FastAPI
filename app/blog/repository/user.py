from fastapi import HTTPException, status
from blog import schemas, models
from blog.hashing import Hash

async def create(request: schemas.User):
    hashed_password = Hash().bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    await new_user.insert()
    return new_user

async def show(id: str):
    user = await models.User.get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not found")
    return user
