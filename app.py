


from flask import Flask, render_template, abort, request, redirect, url_for



from database import (
    get_all_posts,
    get_post,
    get_tags_for_post,
    get_posts_by_tag,
    get_tag,
    create_post,
    get_all_tags
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





@app.route("/post/new", methods=["GET", "POST"])
def new_post():
    tags = get_all_tags()

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        body = request.form.get("body", "").strip()
        selected_tags = request.form.getlist("tags")

        if not title or not body:
            return render_template(
                "post_form.html",
                error="Please fill in both the title and content.",
                title=title,
                body=body,
                tags=tags,
                selected_tags=selected_tags
            ), 400

        valid_tag_ids = {str(tag["id"]) for tag in tags}

        if any(tag_id not in valid_tag_ids for tag_id in selected_tags):
            return render_template(
                "post_form.html",
                error="Please select valid tags.",
                title=title,
                body=body,
                tags=tags,
                selected_tags=[]
            ), 400

        post_id = create_post(title, body, selected_tags)

        return redirect(url_for("post_detail", post_id=post_id))

    return render_template(
        "post_form.html",
        title="",
        body="",
        tags=tags,
        selected_tags=[],
        error=None
    )




if __name__ == "__main__":
    app.run(debug=True)
