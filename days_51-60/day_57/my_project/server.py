from flask import Flask, render_template
import requests
import random
import datetime as dt

app = Flask(__name__)

main_template = "index.html"


@app.route("/")
def home():
    # pass a variable to render_template() AFTER passing the template file
    # the variable should be passed as a keyword arg, so that jinja can access
    #   the variable from within the template file
    random_num = random.randint(1, 10)
    current_year = dt.datetime.now().year
    creator_name = "Dakota Bowman"
    return render_template(main_template, num=random_num, year=current_year, name=creator_name)


@app.route("/guess/<name>")
def guess(name):
    response = requests.get(url=f"https://api.agify.io?name={name}")
    age_str = response.json()["age"]
    name_str = response.json()["name"]
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_str = response.json()["gender"]
    return render_template("guess.html", name=name_str, gender=gender_str, age=age_str)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/fadd5ff9526b8ed9ee1f"
    blog_response = requests.get(url=blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts, rand_num=int(num))


if __name__ == "__main__":
    app.run(debug=True)
