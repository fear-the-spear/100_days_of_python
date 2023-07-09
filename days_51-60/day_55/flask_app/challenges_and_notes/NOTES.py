# NOTE: DO NOT RUN THIS APP. This is just a notes file for notes
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1 style='text-align: center;'>Hello World!</h1>" \
           "<p>This is a paragraph</p>"


@app.route('/bye')
def bye():
    return "Bye"


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there, {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True, )
