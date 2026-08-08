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
    cursor.execute("""SELECT * FROM posts;""")  # Run the query first
    posts = cursor.fetchall()                   # Fetch the actual data rows here
    return {"data": posts}                      # Return the response payload

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,(post.title, post.content, post.published))
    new_post=cursor.fetchone()
    conn.commit()
    return {"data": new_post}

@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return {"details": post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE "id " = %s """, (id,))
    test_post = cursor.fetchone()
    
    if not test_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"post with id: {id} was not found"
        )
        
    return {"post_detail": test_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE "id " = %s RETURNING * """, (id,))
    deleted_post = cursor.fetchone()
    
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exsist")

    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def uppdate_posts(id: int, post: post):
    cursor.execute(
        """UPDATE posts SET title = %s, content = %s, published = %s WHERE "id " = %s RETURNING * """,
        (post.title, post.content, post.published, id)
    )
    updated_post = cursor.fetchone()

    if updated_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"post with id: {id} does not exsist"
        )
    conn.commit()
    return {"data": updated_post}
