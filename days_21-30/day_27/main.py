import tkinter

# Tkinter Labels, Buttons, and Entry (input)

# create window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# create components to put inside window

# Label
# first, specify type
my_label = tkinter.Label(text="I am a label", font=("Courier", 24, "bold"))
# then, specify how component will be laid out on screen
my_label.pack()  # with no arguments, goes to top center

# changing value of 'text'
# 1. access it like a dictionary
my_label["text"] = "New Text"
# 2. use `.config()`
my_label.config(text="Even Newer Text")

# Button
# click function


def click():
    my_label.config(text=input.get())
    # input.get() returns the input from below as a string
    # it can be used inside this function to change the text of any component


# again, specify type
# `command` is listener
button = tkinter.Button(text="Click Me", command=click)
# specify layout on screen
button.pack()

# Entry (an input)
# as always, specify type and then use `.pack()` to place on screen
input = tkinter.Entry(width=10)
input.pack()

# main loop that keeps the gui (window) on-screen
window.mainloop()  # always keep at very end of program
