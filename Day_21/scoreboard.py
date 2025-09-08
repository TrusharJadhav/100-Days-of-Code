from turtle import Turtle
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.current_score=0

        self.penup()
        self.color("white")
        self.goto(0,350)
        self.write(f"score:{self.current_score}", True, align="center",font=('Aerial',12,'bold'))
        self.hideturtle()