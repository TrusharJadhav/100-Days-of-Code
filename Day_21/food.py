from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        x=random.randint(-200,20)
        y=random.randint(-200,200)
        self.goto(x,y)