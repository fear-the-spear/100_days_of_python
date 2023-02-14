import random
import heroes
import turtle as t

ttt = t.Turtle()
ttt.shape("turtle")
ttt.color("SkyBlue")

# # Draw a square
# for _ in range(4):
#     ttt.forward(100)
#     ttt.left(90)

# # Draw a dashed line
# for _ in range(10):
#     ttt.pencolor("black")
#     ttt.forward(10)
#     ttt.penup()
#     ttt.forward(10)
#     ttt.pendown()

# draw shapes with an 'n' number of sides (from 3 to 10)
# colors = ["red", "blue", "yellow", "black", "green", "purple", "MediumAquamarine", "orange", "DarkOrchid",
#           "CornflowerBlue", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "wheat", "SeaGreen"]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     ttt.pencolor(random.choice(colors))
#     for _ in range(num_sides):
#         ttt.pensize(7)
#         ttt.forward(40)
#         ttt.right(angle)


# for shape_side_n in range(3, 10):
#     draw_shape(shape_side_n)

# # draw a random walk
# angles = [0, 90, 180, 270]

# ttt.pensize(10)
# ttt.speed("fastest")
# for _ in range(100):
#     ttt.pencolor(random.choice(colors))
#     angle = random.choice(angles)
#     ttt.forward(20)
#     ttt.right(angle)

# Draw a random walk, but with random RGB colors
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# angles = [0, 90, 180, 270]

# ttt.pensize(10)
# ttt.speed("fastest")
# for _ in range(100):
#     ttt.pencolor(random_color())
#     angle = random.choice(angles)
#     ttt.forward(20)
#     ttt.right(angle)

# Draw a spirograph
ttt.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        ttt.color(random_color())
        ttt.circle(100)
        ttt.setheading(ttt.heading() + size_of_gap)


draw_spirograph(5)


# testing install and import of modules
print(heroes.gen())

# Generate a screen for the turtle, and keep on until click
screen = t.Screen()
screen.exitonclick()
