from turtle import Turtle
import time
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
    def reset_ball(self):
        time.sleep(2)
        self.goto(0,0)
        self.setheading(random.randint(0,45))
    

