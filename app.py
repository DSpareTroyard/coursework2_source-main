from flask import Flask, render_template, request
import utils

app = Flask(__name__)
posts_data = utils.get_posts_data("data/data.json", "data/comments.json")


@app.route("/", methods=['GET'])
def index_page():
    posts = posts_data.get_posts_all()
    comments = posts_data.get_comments()
    posts = utils.get_posts_with_comment_count(posts, comments)
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>/", methods=["GET"])
def post_page(post_id):
    post = posts_data.get_post_by_pk(post_id)
    comments = posts_data.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search/", methods=["GET"])
def search_page():
    s = request.args.get('s')
    posts = posts_data.search_for_posts(s)
    comments = posts_data.get_comments()
    posts = utils.get_posts_with_comment_count(posts, comments)
    return render_template("search.html", s=s, posts=posts)


if __name__ == '__main__':
    app.run()
