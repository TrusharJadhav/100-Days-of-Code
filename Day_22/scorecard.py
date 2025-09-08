from turtle import Turtle, Screen
screen=Screen
screen.setup(width=800,height=600)

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        
        self.goto(0,260)
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
