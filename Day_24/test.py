from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
tim.penup()
score=10
string="Score "+ str(score)
tim.goto(0,350)
tim.write(str(string), True, align="center",font=('Aerial',12,'bold'))
tim.ht()

screen.exitonclick()