import pytest
from PostsData import PostsData
from app import app
import json


def test_load_data():
    assert type(PostsData.load_data("self", "data/data.json")) == list, type(
        PostsData.load_data("self", "data/data.json"))


def test_class_posts_data():
    test_posts_data = PostsData("data/data.json", "data/comments.json")
    assert type(test_posts_data.posts) == list
    assert type(test_posts_data.comments) == list


def test_get_posts_all():
    test_posts_data = PostsData("data/data.json", "data/comments.json")
    assert type(test_posts_data.get_posts_all()) == list


def test_get_comments():
    test_posts_data = PostsData("data/data.json", "data/comments.json")
    assert type(test_posts_data.get_comments()) == list


def test_get_posts_by_user():
    test_posts_data = PostsData("data/data.json", "data/comments.json")
    assert type(test_posts_data.get_posts_by_user('leo')) == list


def test_get_posts_by_post_id():
    test_posts_data = PostsData("data/data.json", "data/comments.json")
    assert type(test_posts_data.get_comments_by_post_id(1)) == list


def test_search_for_posts():
    test_posts_data = PostsData("data/data.json", "data/comments.json")
    assert type(test_posts_data.search_for_posts("A")) == list


def test_get_post_by_pk():
    test_posts_data = PostsData("data/data.json", "data/comments.json")
    assert type(test_posts_data.get_post_by_pk(1)) == dict


def test_app_api_posts_type():
    response = app.test_client().get('/api/posts/')
    assert type(response.json) == list


def test_app_api_posts_keys():
    response = app.test_client().get('/api/posts/')
    needed_keys = ['content', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk']
    for el in response.json:
        for key in needed_keys:
            assert (bool(key in el.keys()) == True), key in el.keys()


def test_app_api_post_type():
    with open("data/data.json", "r", encoding='utf-8') as f:
        p = json.load(f)

    for post in p:
        response = app.test_client().get(f"/api/posts/{post['pk']}/")
        assert type(response.json) == dict, type(response.json)


def test_app_api_post_keys():
    needed_keys = ['content', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk']
    with open("data/data.json", "r", encoding='utf-8') as f:
        p = json.load(f)

    for post in p:
        response = app.test_client().get(f"/api/posts/{post['pk']}/")
        for key in needed_keys:
            assert (bool(key in response.json.keys()) == True), key in response.json.keys()
