FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.increase=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.speed=0
      
        self.write(f"Level: {self.score}",align="center",font=("Arial",24,"normal"))
    def update_score(self):
        self.score+=1
        self.increase+=20
        self.clear()
        self.write(f"Level: {self.score}",align="center",font=("Arial",24,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align="center",font=("Arial",30,"normal"))