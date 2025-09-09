from turtle import Turtle,Screen
import time
from Paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import random
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Ping Pong Game") 
screen.tracer(0)
ball=Ball()
scorecard1=Scorecard()
scorecard1.goto(150,260)
scorecard2=Scorecard()
scorecard2.goto(-150,260)
ball.setheading(random.randint(0,45))
for i in range(20):
    net=Turtle("square")
    net.color("white")
    net.shapesize(stretch_wid=1,stretch_len=0.1)
    net.penup()
    net.goto(0,300-(i*30))
paddle1=Paddle()
paddle1.goto(350,0)
paddle2=Paddle()
paddle2.goto(-350,0)


screen.update()
screen.listen()
game_is_on=True

while game_is_on:
    screen.update()
    ball.forward(1)
    screen.onkey(lambda:paddle1.sety(paddle1.ycor()+20),"Up")
    screen.onkey(lambda:paddle1.sety(paddle1.ycor()-20),"Down")
    screen.onkey(lambda:paddle2.sety(paddle2.ycor()+20),"a")
    screen.onkey(lambda:paddle2.sety(paddle2.ycor()-20),"z")
    #collision with paddle
    if (ball.distance(paddle1)<30 and ball.xcor()>340) or (ball.distance(paddle2)<30 and ball.xcor()<-340):
        ball.setheading(180-ball.heading())
    #collision with wall
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.setheading(-ball.heading())
    #missed by paddle
    if ball.xcor()>390:
        scorecard2.update_score()
        time.sleep(2)
        ball.goto(0,0)
        ball.setheading(random.randint(0,360))
    if ball.xcor()<-390:
        scorecard1.update_score()
        time.sleep(2)
        ball.goto(0,0)
        ball.setheading(random.randint(0,360))
    if scorecard1.score==5 or scorecard2.score==5:
        game_is_on=False
        ball.hideturtle()
        if scorecard1.score==5:
            scorecard1.goto(0,0)
            scorecard1.write("Player 1 Wins!",align="center",font=("Arial",30,"normal"))
        else:
            scorecard2.goto(0,0)
            scorecard2.write("Player 2 Wins!",align="center",font=("Arial",30,"normal"))
screen.exitonclick()

