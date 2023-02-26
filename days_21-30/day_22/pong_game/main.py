from turtle import Screen
from paddle import Paddle
from pong_ball import PongBall
from scoreboard import Scoreboard
import time

# screen setup (size, color, title, animation on/off)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)  # turn off screen animation

# create both left and right paddles, with coordinates passed as arguments
l_paddle = Paddle(position=(-350, 0))
r_paddle = Paddle(position=(350, 0))

# create pong ball
ball = PongBall()

# create score board
scoreboard = Scoreboard()

# listen for key presses
screen.listen()

# assign keys to up and down functions for each paddle (left and right)
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# game logic
is_game_on = True

while is_game_on:
    screen.update()  # pairs w/ .tracer(0) to make turtle visible
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when right paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # detect when left paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()


# set screen to only exit on click
# NOTE: when game is in while loop,
#       screen only closes upon clicking 'close' btn
screen.exitonclick()
