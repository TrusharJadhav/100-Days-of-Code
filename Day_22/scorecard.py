from turtle import Turtle, Screen

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(50,260)
        self.hideturtle()
#       self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))    