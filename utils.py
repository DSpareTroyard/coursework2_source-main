from PostsData import PostsData


def get_posts_data(posts_path, comments_path, bookmarks_path):
    posts_data = PostsData(posts_path, comments_path, bookmarks_path)
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


def get_content_with_tags(post_content):
    post_content = post_content.split()
    content = []
    for word in post_content:
        if "#" in word:
            if word[0] != "#":
                temp_word = word.split("#")
                content.append(temp_word[0])
                word = f'#{temp_word[1]}'

            temp_word = f'<a href="/tag/{word[1:].lower()}/">{word}</a>'
            content.append(temp_word)
        else:
            content.append(word)
    return " ".join(content)
