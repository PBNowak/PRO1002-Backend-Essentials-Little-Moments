

from flask import Flask, render_template, abort
from database import get_all_posts, get_post


app = Flask(__name__)


@app.route("/")
def home():
    posts = get_all_posts()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = get_post(post_id)

    if post is None:
        abort(404)

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
