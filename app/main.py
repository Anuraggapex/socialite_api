from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body 
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time



class post(BaseModel):
    title : str
    content : str 
    published : bool = True
    rating: Optional[int]=None

while True:

    try:
        conn=psycopg2.connect(host='localhost', database='fastapi', user="postgres",password='Pavu@2631', cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was sucessfull")
        break
    except Exception as error:
        print("connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

app = FastAPI()

my_posts=[{"title":"title of post 1", "content":"content of post 1", "id":1}, {"title":"favourite foods","content" :"i like pizza", "id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def read_root():
    return {"message": "Helo World"}

@app.get("/posts")
def get_posts():
    posts = cursor.execute("""SELECT * FROM posts """)  
    posts=cursor.fetchall()
    return {"data": posts}
     
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return {"details": post}


@app.get("/posts/{id}")
def get_post(id: int):
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found ")

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exsist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def uppdate_posts(id: int, post: post):
    index=find_index_post(id)

    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exsist")

    post_dict=post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict
    return{"data": post_dict}

    
