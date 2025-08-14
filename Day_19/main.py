from turtle import Turtle, Screen
screen=Screen()
tim=Turtle()

def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def clockwise():
    tim.right(10)
    tim.forward(10)
def anticlockwise():
    tim.left(10)
    tim.forward(10)
def clear():
    tim.reset()
screen.listen()

screen.onkey(key="Right",fun=forward)
screen.onkey(key="Left",fun=backward)
screen.onkey(key="Up",fun=anticlockwise)
screen.onkey(key="Down ",fun=clockwise)
screen.onkey(key="c",fun=clear)



screen.exitonclick()

    
