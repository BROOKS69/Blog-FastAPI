from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {"data": "blog list"}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}  

@app.post('/blog/photos')    
def photos():
    return {'data': 'all photo posted here'}      

@app.get('/blog/{id}')
def show(id: int):
    # This function retrieves a blog post by its ID.
    return {'data': id}    

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}  

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created as {request.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000) 