from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align="center",
                   font=("Courier", 14, "normal"))

    def go_to_next_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("#d11717")
        self.write("GAME OVER.", align="center", font=(
            "FiraCode Nerd Font Mono", 30, "bold"))
