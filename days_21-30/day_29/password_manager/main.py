from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []


def gen_pass():
    '''
    Generates a password from a combination of 8-10 letters,
    2-4 numbers, and 2-4 symbols. It then copies the password
    to the clipboard for easy pasting into a web form.'''
    ltrs = [choice(letters) for _ in range(randint(8, 10))]
    smbls = [choice(symbols) for _ in range(randint(2, 4))]
    nmbrs = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = ltrs + smbls + nmbrs

    shuffle(password_list)

    password = "".join(password_list)

    passwd_entry.delete(0, END)
    passwd_entry.insert(0, password)
    passwd_entry.clipboard_clear()
    passwd_entry.clipboard_append(passwd_entry.get())
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    '''
    'Save' button-press functionality:

    Saves user-entered data from all data fields into a
    file called 'data.txt' - unless one or more fields is empty.
    '''
    web_addr = web_entry.get()
    email = user_entry.get()
    passwd = passwd_entry.get()

    if len(web_addr) == 0 or len(passwd) == 0:
        messagebox.showinfo(
            title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=web_addr, message=f"These are the details entered:\n\nEmail: {email}\nPassword: {passwd}\n\nIs it okay to save?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"\n{web_addr} | {email} | {passwd}")
                web_entry.delete(0, END)
                passwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=75, pady=75)

# Canvas Setup & Background Image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website")
web_label.grid(column=0, row=1)
user_label = Label(text="Email/Username")
user_label.grid(column=0, row=2)
passwd_label = Label(text="Password")
passwd_label.grid(column=0, row=3)

# Text Boxex
web_entry = Entry(width=37)
web_entry.grid(column=1, row=1, columnspan=2)
user_entry = Entry(width=37)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(END, "dakotabbowman@outlook.com")
passwd_entry = Entry(width=21)
passwd_entry.grid(column=1, row=3)

# Generate Password Button
generate_btn = Button(text="Generate Password", width=11, command=gen_pass)
generate_btn.grid(column=2, row=3)

# Add Button
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
