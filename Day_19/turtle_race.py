from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=600,height=400)
user_bet=screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Eneter a color:")
color=["red","orange","yellow","green","blue","purple"]
turtles=[]

def start_race():
    y=[150,100,50,0,-50,-100,-150]
    for i in range(6):
        Tim=Turtle(shape="turtle")
        Tim.color(color[i])
        Tim.penup()
        Tim.goto(-250,y[i])
        turtles.append(Tim)
def check_winner():
    distance=[]
    for j in range(6):
        tim=turtles[j]
        distance.append(tim.pos()[0])
    winner=max(distance)
    
    if winner >= 100:
        position=distance.index(winner)
        if user_bet==color[position]:
            print(f"You win, winner is {color[position]}")
        else:
            print(f"You Lose, winner is {color[position]}") 
        return False  
    else:
        return True
start_race()
def race():
    race_On=True
    while race_On:
        for j in range(6):
            speed=random.randint(0,10)
            tim=turtles[j]
            tim.forward(speed)
        race_On=check_winner()
        

race()

    



screen.exitonclick()