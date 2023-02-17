# Etch-A-Sketch
from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forward():
    tom.fd(10)


def move_backwards():
    tom.backward(10)


def counter_clockwise():
    tom.left(10)


def clockwise():
    tom.right(10)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
