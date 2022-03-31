from flask import Flask, render_template, request, jsonify
import utils, json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
posts_data = utils.get_posts_data("data/data.json", "data/comments.json")


@app.route("/", methods=['GET'])
def index_page():
    posts = posts_data.get_posts_all()
    comments = posts_data.get_comments()
    with open("data/bookmarks.json", encoding='utf-8') as f:
        bookmarks = json.load(f)
    posts = utils.get_posts_with_comment_count(posts, comments)

    return render_template("index.html", posts=posts, bookmarks=bookmarks)


@app.route("/posts/<int:post_id>/", methods=["GET"])
def post_page(post_id):
    post = posts_data.get_post_by_pk(post_id)
    comments = posts_data.get_comments_by_post_id(post_id)
    content = utils.get_content_with_tags(post['content'])
    return render_template("post.html", post=post, comments=comments, content=content)


@app.route("/search/", methods=["GET"])
def search_page():
    s = request.args.get('s')
    posts = posts_data.search_for_posts(s)
    comments = posts_data.get_comments()
    posts = utils.get_posts_with_comment_count(posts, comments)

    return render_template("search.html", s=s, posts=posts)


@app.route("/users/<username>/")
def user_page(username):
    posts = posts_data.get_posts_by_user(username)
    comments = posts_data.get_comments()
    posts = utils.get_posts_with_comment_count(posts, comments)
    return render_template("user-feed.html", posts=posts, username=username)


@app.route("/api/posts/", methods=["GET"])
def api_posts_page():
    posts = posts_data.get_posts_all()
    return jsonify(posts)


@app.route("/api/posts/<int:post_id>/", methods=["GET"])
def api_single_post_page(post_id):
    post = posts_data.get_post_by_pk(post_id)
    return jsonify(post)


@app.route("/tag/<tag_name>/")
def tag_page(tag_name):
    posts = posts_data.search_for_posts(f'#{tag_name}')
    comments = posts_data.get_comments()
    posts = utils.get_posts_with_comment_count(posts, comments)
    return render_template("tag.html", posts=posts, tag_name=tag_name)


if __name__ == '__main__':
    app.run()
