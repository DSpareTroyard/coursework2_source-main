from flask import Flask, render_template, request, jsonify, redirect
import utils

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
posts_data = utils.get_posts_data("data/data.json", "data/comments.json", "data/bookmarks.json")
bookmarks = posts_data.get_bookmarks()


@app.route("/", methods=['GET'])
def index_page():
    posts = posts_data.get_posts_all()
    comments = posts_data.get_comments()
    posts = utils.get_posts_with_comment_count(posts, comments)

    return render_template("index.html", posts=posts, bookmarks=bookmarks)


@app.route("/posts/<int:post_id>/", methods=["GET"])
def post_page(post_id):
    post = posts_data.get_post_by_pk(post_id)
    comments = posts_data.get_comments_by_post_id(post_id)
    content = utils.get_content_with_tags(post['content'])
    return render_template("post.html", post=post, comments=comments, content=content, bookmarks=bookmarks)


@app.route("/search/", methods=["GET"])
def search_page():
    s = request.args.get('s')
    posts = posts_data.search_for_posts(s)
    comments = posts_data.get_comments()
    posts = utils.get_posts_with_comment_count(posts, comments)

    return render_template("search.html", s=s, posts=posts, bookmarks=bookmarks)


@app.route("/users/<username>/")
def user_page(username):
    posts = posts_data.get_posts_by_user(username)
    comments = posts_data.get_comments()
    posts = utils.get_posts_with_comment_count(posts, comments)
    return render_template("user-feed.html", posts=posts, username=username, bookmarks=bookmarks)


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
    return render_template("tag.html", posts=posts, tag_name=tag_name, bookmarks=bookmarks)


@app.route("/bookmarks/add/<int:post_id>/")
def add_bookmark_page(post_id):
    if post_id not in bookmarks:
        bookmarks.append(post_id)

    posts_data.update_bookmarks(bookmarks)
    return redirect("/", code=302)


@app.route("/bookmarks/remove/<int:post_id>/")
def remove_bookmark_page(post_id):
    if post_id in bookmarks:
        bookmarks.remove(post_id)

    posts_data.update_bookmarks(bookmarks)
    return redirect("/", code=302)


@app.route("/bookmarks/")
def bookmarks_page():
    posts = posts_data.get_posts_in_bookmarks()
    comments = posts_data.get_comments()
    posts = utils.get_posts_with_comment_count(posts, comments)

    return render_template("bookmarks.html", posts=posts, bookmarks=bookmarks)


if __name__ == '__main__':
    app.run()
