

from flask import Flask, render_template, abort

from database import (
    get_all_posts,
    get_post,
    get_tags_for_post,
    get_posts_by_tag,
    get_tag
)




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

    tags = get_tags_for_post(post_id)

    return render_template(
        "post.html",
        post=post,
        tags=tags
    )



@app.route("/tag/<int:tag_id>")
def tag_posts(tag_id):
    tag = get_tag(tag_id)

    if tag is None:
        abort(404)

    posts = get_posts_by_tag(tag_id)

    return render_template(
        "tag.html",
        posts=posts,
        tag=tag
    )



if __name__ == "__main__":
    app.run(debug=True)
