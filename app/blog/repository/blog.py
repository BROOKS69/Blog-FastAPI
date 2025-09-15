from fastapi import HTTPException, status, Response
from blog import schemas, models

async def get_all():
    blogs = await models.Blog.find_all().to_list()
    for blog in blogs:
        await blog.fetch_link(models.Blog.creator)
    return blogs

async def create(request: schemas.Blog, user_id: str):
    user = await models.User.get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    new_blog = models.Blog(title=request.title, body=request.body, creator=user)
    await new_blog.insert()
    return new_blog

async def destroy(id: str):
    blog = await models.Blog.get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    await blog.delete()
    return 'done'

async def update(id: str, request: schemas.Blog):
    blog = await models.Blog.get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    blog.title = request.title
    blog.body = request.body
    await blog.save()
    return 'updated'

async def show(id: str):
    blog = await models.Blog.get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    await blog.fetch_link(models.Blog.creator)
    return blog
