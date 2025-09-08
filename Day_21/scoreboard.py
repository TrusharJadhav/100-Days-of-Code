from turtle import Turtle
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
    def score(self):
        self.write("Score: ",True,align="Center")