import pytest
from app import schemas

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    assert res.status_code == 200
    assert len(res.json()) == len(test_posts)

def test_unauthorized_user_get_all_posts(client):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_create_post(authorized_client, test_user):
    post_data = {"title": "Test Title", "content": "Test Content", "published": True}
    res = authorized_client.post("/posts/", json=post_data)
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == post_data["title"]
    assert created_post.owner_id == test_user["id"]