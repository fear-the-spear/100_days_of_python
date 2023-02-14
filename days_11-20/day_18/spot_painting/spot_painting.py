import colorgram as cg
import turtle as t
import random

ttt = t.Turtle()
screen = t.Screen()

# NOTE: The code below is commented out because it was only used to
#       take a picture as input and return 'n' colors, then convert
#       the returned objects to a list of tuples

# colors = cg.extract("spot_painting/hirst-spot-painting.jpg", 30)

# rgb_colors = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb_colors.append((red, green, blue))

# print(rgb_colors)

colors_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71),
               (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

t.colormode(255)
t.speed("fastest")
t.hideturtle()
pos = 0


def ten_across():
    random_color = random.choice(colors_list)
    ttt.pencolor(random_color)
    ttt.dot(14)
    ttt.penup()
    ttt.fd(35)


for _ in range(10):
    for _ in range(10):
        ten_across()
    pos += 35
    ttt.sety(pos)
    ttt.setx(0)

screen.exitonclick()
