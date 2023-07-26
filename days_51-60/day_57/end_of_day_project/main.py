from flask import Flask, render_template
import requests as req

from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    posts = Post().get_posts()
    return render_template("index.html", all_posts=posts)

@app.route("/blog/<post_index>")
def get_blog(post_index):
    index = int(post_index) - 1
    print(index)
    title = Post().get_posts()[index]['title']
    subtitle = Post().get_posts()[index]['subtitle']
    body = Post().get_posts()[index]['body']
    return render_template("post.html", title=title, subtitle=subtitle, body=body)

if __name__ == "__main__":
    app.run(debug=True)
