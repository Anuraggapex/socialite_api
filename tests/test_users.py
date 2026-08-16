import pytest
from app import schemas

def test_create_user(client):
    res = client.post("/users/", json={"email": "newuser@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert res.status_code == 201
    assert new_user.email == "newuser@gmail.com"

def test_create_user_duplicate_email(client, test_user):
    res = client.post("/users/", json={"email": test_user["email"], "password": "password123"})
    assert res.status_code == 400