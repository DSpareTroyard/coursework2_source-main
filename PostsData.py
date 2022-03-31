import json


class PostsData:
    def __init__(self, posts_path, comments_path):
        self.posts = self.load_data(posts_path)
        self.comments = self.load_data(comments_path)

    def load_data(self, path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)

    def get_posts_all(self):
        return self.posts

    def get_comments(self):
        return self.comments

    def get_posts_by_user(self, user_name):
        filtered_posts = []
        for post in self.posts:
            if user_name in post['poster_name']:
                filtered_posts.append(post)

        return filtered_posts

    def get_comments_by_post_id(self, post_id):
        filtered_comments = []
        for comment in self.comments:
            if post_id == comment['post_id']:
                filtered_comments.append(comment)

        return filtered_comments

    def search_for_posts(self, query):
        filtered_posts = []
        for post in self.posts:
            if query.lower() in post['content'].lower():
                filtered_posts.append(post)

        if len(filtered_posts) > 10:
            filtered_posts = filtered_posts[:10]

        return filtered_posts

    def get_post_by_pk(self, pk):
        for post in self.posts:
            if post['pk'] == pk:
                return post
