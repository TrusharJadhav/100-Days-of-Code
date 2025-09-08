from turtle import Turtle,Screen
import time
#from scorecard import Scorecard
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Ping Pong Game") 
screen.tracer(0)
for i in range(20):
    net=Turtle("square")
    net.color("white")
    net.shapesize(stretch_wid=1,stretch_len=0.1)
    net.penup()
    net.goto(0,300-(i*30))
paddle=Turtle("square")
paddle.color("white")
paddle.penup()
paddle.goto(350,0)
paddle.shapesize(stretch_wid=5,stretch_len=1)
screen.update()
screen.listen()
game_is_on=True

while game_is_on:
    screen.update()
    screen.onkey(lambda:paddle.sety(paddle.ycor()+20),"Up")
    screen.onkey(lambda:paddle.sety(paddle.ycor()-20),"Down")

screen.exitonclick()

