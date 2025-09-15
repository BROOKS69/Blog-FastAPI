from fastapi import APIRouter, status
from blog import schemas
from blog.repository import user

router = APIRouter(
    prefix="/user",
)

@router.post('/', response_model=schemas.ShowUser, tags=["USERS"])
async def create_user(request: schemas.User):
    return await user.create(request)

@router.get('/{id}', response_model=schemas.ShowUser, tags=["USERS"])
async def get_user(id: str):
   return await user.show(id)
