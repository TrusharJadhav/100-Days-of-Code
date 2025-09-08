from turtle import Turtle
ALIGNMENT="center"
FONT=('Aerial',24,'normal')
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.current_score=0

        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.write(f"score:{self.current_score}", align=ALIGNMENT,font=FONT)
    def increase_score(self):
        self.current_score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)
