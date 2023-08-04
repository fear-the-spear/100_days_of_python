from flask import Flask, render_template
import requests

app = Flask(__name__)

res = requests.get(url="https://api.npoint.io/e7237338994b5a7cfb0e")
posts = res.json()


@app.route("/")
def home():
    content = posts
    return render_template("index.html", posts=content)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<post_index>")
def get_post(post_index):
    index = int(post_index) - 1
    title = posts[index]["title"]
    print(title)
    subtitle = posts[index]["subtitle"]
    print(subtitle)
    body = posts[index]["body"]
    print(body)
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug="True")
