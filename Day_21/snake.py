from turtle import Turtle,Screen
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __int__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITION:
            seg=Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(position)
            self.segments.append(seg)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            position=self.segments[seg_num-1].pos()
            self.segments[seg_num].goto(position)
            head=self.segments[0]
            head.forward(MOVE_DISTANCE)
            head.left(90)





