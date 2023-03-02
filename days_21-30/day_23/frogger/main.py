from turtle import Screen
from frog import Frog
from car import CarManager
from scoreboard import Scoreboard
import random
import time

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Frogger")
screen.tracer(0)

# create user character, which will be shaped as a turtle but called a frog
frog = Frog()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(frog.move_up, "Up")

# game logic
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if frog.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if frog.is_at_finish_line():
        frog.go_to_start()
        car_manager.level_up()
        scoreboard.go_to_next_level()

# set screen to only exit on click
# NOTE: when game is in while loop,
#       screen only closes upon clicking 'close' btn
screen.exitonclick()
