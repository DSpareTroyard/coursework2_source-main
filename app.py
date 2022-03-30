from flask import Flask, render_template
import utils

app = Flask(__name__)
posts_data = utils.get_posts_data("data/data.json", "data/comments.json")


@app.route("/", methods=['GET'])
def index_page():
    posts = posts_data.get_posts_all()
    comments = posts_data.get_comments()
    posts = utils.get_comments_count(posts, comments)
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:postid>", methods="GET")
def post_page(post_id):
    post = posts_data.get_post_by_pk(post_id)
    comments = posts_data.get_comments_by_post_id(post_id)


if __name__ == '__main__':
    app.run()
