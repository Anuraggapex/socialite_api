from typing import List
from fastapi import Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas
from ..database import get_db

router=APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("",response_model=List[schemas.post_response])
def get_posts(db:Session=Depends(get_db)):
    posts=db.query(models.post).all()
    return posts

@router.post("",status_code=status.HTTP_201_CREATED,response_model=schemas.post_response)
def create_posts(post:schemas.post_create,db:Session=Depends(get_db)):
    new_post=models.post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/latest",response_model=schemas.post_response)
def get_latest_post(db:Session=Depends(get_db)):
    latest_post=db.query(models.post).order_by(models.post.id.desc()).first()
    return latest_post

@router.get("/{id}",response_model=schemas.post_response)
def get_post(id:int,db:Session=Depends(get_db)):
    test_post=db.query(models.post).filter(models.post.id==id).first()

    if not test_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found"
        )

    return test_post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db)):
    post_query=db.query(models.post).filter(models.post.id==id)
    deleted_post=post_query.first()

    if deleted_post==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exsist"
        )

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.post_response)
def uppdate_posts(id:int,updated_post:schemas.post_create,db:Session=Depends(get_db)):
    post_query=db.query(models.post).filter(models.post.id==id)
    target_post=post_query.first()

    if target_post==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exsist"
        )

    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()
