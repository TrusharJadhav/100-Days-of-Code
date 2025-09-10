from turtle import Turtle
ALIGNMENT="center"
FONT=('Aerial',24,'normal')
with open("high_score.txt","r") as file:
    content=file.read()
    high_score=int(content)
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
        self.write(f"score:{self.current_score} High Score: {high_score}", align=ALIGNMENT,font=FONT)
    def increase_score(self):
        self.current_score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)
    def update_high_score(self):
        if self.current_score>high_score:
            with open("high_score.txt","w") as file:
                self.goto(0,50)
                self.write(f"CONGRATULATION ! You have set new high score of {self.current_score}", align=ALIGNMENT,font=FONT)
                file.write(str(self.current_score))
        
