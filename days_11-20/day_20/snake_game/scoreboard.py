from turtle import Turtle
ALIGNMENT = "center"
FONT = ('American Typewriter', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
