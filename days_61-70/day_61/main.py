from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from form import MyForm

# initialize app
app = Flask(__name__)
# initialize template with app inserted
bootstrap = Bootstrap5(app)

app.secret_key = "this-is--my---secret----key"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
