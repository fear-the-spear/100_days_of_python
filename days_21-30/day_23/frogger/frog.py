from turtle import Turtle
FINISH_LINE_Y = 260
MOVE_DISTANCE = 10
STARTING_POSITION = (0, -265)


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        '''moves character up by a set distance'''
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        '''places character at the initial starting position'''
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
