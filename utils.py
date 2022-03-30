from PostsData import PostsData


def get_posts_data(posts_path, comments_path):
    posts_data = PostsData(posts_path, comments_path)
    return posts_data


def get_posts_with_comment_count(posts, comments):
    new_posts = []
    for post in posts:
        post['comment_count'] = 0
        for comment in comments:
            if comment['post_id'] == post['pk']:
                post['comment_count'] += 1

        new_posts.append(post)

    return new_posts
