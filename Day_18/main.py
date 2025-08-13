from turtle import Turtle, Screen  
import random
turtle_colors = [
    'alice blue', 'antique white', 'aquamarine', 'azure', 'beige',
    'bisque', 'black', 'blanched almond', 'blue', 'blue violet',
    'brown', 'burlywood', 'cadet blue', 'chartreuse', 'chocolate',
    'coral', 'cornflower blue', 'cornsilk', 'cyan', 'dark blue',
    'dark cyan', 'dark goldenrod', 'dark gray', 'dark green',
    'dark khaki', 'dark magenta', 'dark orange', 'dark orchid',
    'dark red', 'dark salmon', 'dark sea green', 'dark slate gray',
    'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue',
    'dim gray', 'dodger blue', 'firebrick', 'floral white',
    'forest green', 'gold', 'goldenrod', 'gray', 'green', 'green yellow',
    'honeydew', 'hot pink', 'indian red', 'ivory', 'khaki',
    'lavender', 'lavender blush', 'lawn green', 'lemon chiffon',
    'light blue', 'light coral', 'light cyan', 'light goldenrod yellow',
    'light gray', 'light green', 'light pink', 'light salmon',
    'light sea green', 'light sky blue', 'light slate gray',
    'light steel blue', 'light yellow'
]

tim=Turtle()
screen=Screen()
screen.colormode(255)


tim.shape("arrow")
def geometry():
    for i in range(3,11):
        tim.color(random.choice(turtle_colors))
        for j in range(i):
            angle=180-180*(i-2)/i

            tim.forward(100)
            tim.rt(angle)
def random_walk():
    tim.speed(10)
    for _ in range(3,200):
        tim.pensize(10)
        color_tuple=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tim.color(color_tuple)
        tim.rt(random.choice([0,90,180,270]))
        tim.forward(30)
def spirograph():
    tim.speed("fastest")
    for n in range(360):
        tim.rt(n)
        color_tuple=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tim.color(color_tuple)
        tim.circle(100)
    
#geometry()   
#random_walk()  
spirograph()




screen.exitonclick()