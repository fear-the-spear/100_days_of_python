from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
passwd_entry = Entry(width=21)
passwd_entry.grid(column=1, row=3)

# Generate Password Button
generate_btn = Button(text="Generate Password", width=11)
generate_btn.grid(column=2, row=3)

# Add Button
add_btn = Button(text="Add", width=35)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
