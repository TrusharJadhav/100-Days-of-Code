import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
cars=CarManager()
player=Player()
scoreboard=Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.onkey(lambda:player.forward(10),"Up")
    screen.onkey(lambda:player.forward(-10),"Down")
    cars.move(scoreboard.score*cars.MOVE_INCREMENT)
    if random.randint(1,6)==1:
        cars.launch_car()
    #level 
    if player.ycor()==280:
        scoreboard.update_score()
        player.goto(0,-300)
    screen.update()
    #collusion with cars
    for car in cars.cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on=False


screen.exitonclick()
