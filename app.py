from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index_page():
    posts = utils.get_posts_all("data/data.json")
    comments = utils.get_posts_all("data/comments.json")
    posts = utils.get_comments_count(posts, comments)
    return render_template("index.html", posts=posts)


if __name__ == '__main__':
    app.run()
