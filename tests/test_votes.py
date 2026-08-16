import pytest

def test_vote_on_post(authorized_client, test_posts):
    res = authorized_client.post("/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 201

def test_vote_twice_on_post(authorized_client, test_posts):
    authorized_client.post("/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    res = authorized_client.post("/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 409

def test_delete_vote(authorized_client, test_posts):
    authorized_client.post("/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    res = authorized_client.post("/vote/", json={"post_id": test_posts[0].id, "dir": 0})
    assert res.status_code == 201