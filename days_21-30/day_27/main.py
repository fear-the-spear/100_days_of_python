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
# changing value of 'text'
# 1. access it like a dictionary
# my_label["text"] = "Text"
# 2. use `.config()`
my_label.config(text="New Text")
# then, specify how component will be laid out on screen
my_label.grid(column=0, row=0)

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
button.grid(column=1, row=1)

button_2 = tkinter.Button(text="Another Button")
button_2.grid(column=2, row=0)

# Entry (an input)
# as always, specify type and then use `.pack()` to place on screen
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

# main loop that keeps the gui (window) on-screen
window.mainloop()  # always keep at very end of program

# NOTE: There are 3 ways to lay out widgets (components) on screen:
#         `.pack()` uses the `side` attribute
#            - not specific enough if you have lots of widgets
#         `.place()` uses coordinates
#            - too specific in most cases
#         `.grid()` divides screen into any num of rows and columns
#            - this is overall the best way to lay out widgets
#            - all items are placed relative to each others' positions
#
#       Also, you CANNOT mix grid with the other methods!
