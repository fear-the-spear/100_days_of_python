
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
ORIG_CSV_FILE = "./data/french_words.csv"
NEW_CSV_FILE = "./data/french_words.csv"
# --------------------------------- CSV DATA --------------------------------- #
word_dict = {}

try:
    data = pandas.read_csv(NEW_CSV_FILE)
except FileNotFoundError:
    original_data = pandas.read_csv(ORIG_CSV_FILE)
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")

# ---------------------------------- TIMER ----------------------------------- #


def count_down():
    window.after(3000, flip_card)


# -------------------------------- FLIP CARDS -------------------------------- #
current_card = {}


def next_card():
    '''generates a new french word; sets 'card_title' to 'French' '''
    count_down()
    global current_card
    current_card = random.choice(word_dict)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")


def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(
        card_warning, text="Click 'X' to keep this word in the list and go to the next one.")
    window.after_cancel(count_down)


def is_known():
    word_dict.remove(current_card)
    data = pandas.DataFrame(word_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# --------------------------------- UI SETUP --------------------------------- #
# Window Setup
window = Tk()
window.title("Flashy - The Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Setup (Background Images and Text)
canvas = Canvas(width=800, height=555,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png", height=526, width=800)
card_back = PhotoImage(file="./images/card_back.png", height=526, width=800)
card = canvas.create_image(400, 290, image=card_front)
card_title = canvas.create_text(400, 180, fill="black",
                                text="Language", font="Ariel 65 italic")
card_word = canvas.create_text(400, 300, fill="black",
                               text="word", font="Ariel 100 bold")
card_warning = canvas.create_text(
    400, 450, fill="white", text="", font="Ariel 22 bold italic")
canvas.grid(column=0, row=0, columnspan=3)

# Buttons
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0,
                   border=0, command=is_known)
right_btn.grid(column=0, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0,
                   border=0, command=next_card)
wrong_btn.grid(column=2, row=1)

next_card()
count_down()

window.mainloop()
