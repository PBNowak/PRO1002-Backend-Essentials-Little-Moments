
from flask import Flask, render_template
from database import get_all_posts

app = Flask(__name__)


@app.route("/")
def home():
    posts = get_all_posts()
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
