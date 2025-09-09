COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.STARTING_MOVE_DISTANCE = 10
        self.MOVE_INCREMENT = 5
        self.cars=[]
        self.track=[-250,-200,-150,-100,-50,0,50,100,150,200,250]
    def launch_car(self):
        car=Turtle()
        car.shape("square")
        car.shapesize(stretch_len=2,stretch_wid=1)
        color=random.choice(COLORS)
        car.color(color)
        car.penup()
        car.setheading(180)
        
        car.goto(300,random.choice(self.track))
        self.cars.append(car)
    def move(self,INCREMENT):
        for car in self.cars:
            car.forward(self.STARTING_MOVE_DISTANCE+INCREMENT)
    
    




