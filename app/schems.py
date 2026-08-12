from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class post_base(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

class post_create(post_base):
    pass

class post_response(post_base):
    id:int
    created_at:datetime

    class Config:
        orm_mode=True
