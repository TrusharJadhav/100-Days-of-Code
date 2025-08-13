import colorgram
from turtle import Turtle,Screen
import random
tim=Turtle()
screen=Screen()
screen.screensize(200,200)
screen.colormode(255)
tim.penup()
colors=colorgram.extract('Day_18/spot.jpg',80)
tim.teleport(-200,-200)
dot=100
tim.speed("fastest")
for i in range(1,dot+1):
    col=random.choice(colors).rgb
    tim.dot(20,col)
    tim.forward(50)
    if i%10==0:
        tim.back(500)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(0)
    

screen.exitonclick()
