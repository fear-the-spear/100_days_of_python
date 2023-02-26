from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from score_keeper import ScoreKeeper
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
record_score = ScoreKeeper()
player = screen.textinput(
    title="Welcome to the classic Snake Game!", prompt="Please enter your initials: ")

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if head collides with any segment in tail: trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

record_score.record_score(user_name=player, score=scoreboard.score)

screen.exitonclick()