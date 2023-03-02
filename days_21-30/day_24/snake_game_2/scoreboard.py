from turtle import Turtle
ALIGNMENT = "center"
FONT = ('American Typewriter', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = self.read_high_score()
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as new_high_score:
                new_high_score.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_high_score(self):
        with open("high_score.txt", "r") as read_high_score:
            return int(read_high_score.read())
