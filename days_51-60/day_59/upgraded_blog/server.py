from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

res = requests.get(url="https://api.npoint.io/e7237338994b5a7cfb0e")
posts = res.json()


@app.route("/")
def home():
    content = posts
    return render_template("index.html", posts=content)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(
                user="dakotabbowman@gmail.com",
                password="ftdtofpghfwsrgsr")
            connection.sendmail(
                from_addr="dakotabbowman@gmail.com",
                to_addrs="py.stuff@yahoo.com",
                msg=f"Subject: Great Success!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )
        return render_template("contact.html", is_sent=True)
    return render_template("contact.html", is_sent=False)


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
