import json


def get_posts_all(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def get_posts_by_user(posts, user_name):
    filtered_posts = []
    for post in posts:
        if user_name in post['poster_name']:
            filtered_posts.append(post)

    return filtered_posts


def get_comments_by_post_id(comments, post_id):
    filtered_comments = []
    for comment in comments:
        if post_id == comment['post_id']:
            filtered_comments.append(comment)

    return filtered_comments


def search_for_posts(posts, query):
    filtered_posts = []
    for post in posts:
        if query in post['content']:
            filtered_posts.append(post)

    return filtered_posts


def get_post_by_pk(posts, pk):
    for post in posts:
        if post['pk'] == pk:
            return post


def get_comments_count(posts, comments):
    new_posts = []
    for post in posts:
        post['comment_count'] = 0
        for comment in comments:
            if comment['post_id'] == post['pk']:
                post['comment_count'] += 1

        new_posts.append(post)

    return new_posts
