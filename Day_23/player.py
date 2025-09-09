from turtle import Turtle
START=(0,-300)
MOVE_DISTANCE=50
END=(0,280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.goto(START)
        self.setheading(90)
    def up(self):
        self.forward(MOVE_DISTANCE)
    def down(self):
        self.forward(-MOVE_DISTANCE)
