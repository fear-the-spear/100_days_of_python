from flask import Flask
import random

app = Flask(__name__)
rand_num = random.randint(0, 9)


@app.route("/")
def home():
    return "<h1>Guess a Number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif', alt='count up starting at 0 and ending at 9' />"


@app.route("/<int:guess>")
def guessed_num(guess):
    rand_number = random.randint(0, 9)
    if guess < rand_number:
        return "<h1>Too Low, Try Again!</h1>" \
               "<div style='width:100%;height:0;padding-bottom:83%;position:relative;'><iframe src='https://giphy.com/embed/8UGoOaR1lA1uaAN892' width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div><p><a href='https://giphy.com/gifs/foxsearchlight-8UGoOaR1lA1uaAN892'>via GIPHY</a></p>"
    elif guess > rand_number:
        return "<h1>Too High, Try Again!</h1>" \
               "<div style='width:100%;height:0;padding-bottom:83%;position:relative;'><iframe src='https://giphy.com/embed/8UGoOaR1lA1uaAN892' width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div><p><a href='https://giphy.com/gifs/foxsearchlight-8UGoOaR1lA1uaAN892'>via GIPHY</a></p>"
    else:
        return "<h1>You Got It!</h1>"


if __name__ == "__main__":
    app.run(debug=True, )
