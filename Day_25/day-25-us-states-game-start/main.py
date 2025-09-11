from turtle import Turtle, Screen
import pandas as pd
screen=Screen()
tim=Turtle()
writer=Turtle()
score=Turtle()
score.penup()
score.color("black")
score.goto(0,250)
writer.penup()
screen.bgpic("./blank_states_img.gif")
screen.title("State guessing Game")
states=pd.read_csv("50_states.csv")
Current_score=0
game_is_on=True
while game_is_on:
    answer=screen.textinput(title="Guess the State", prompt="What's another state name")
    print(states.state.values.tolist())
    if answer in states.state.values.tolist():
        cord=states[states["state"]==answer]
        goto_cord=cord.values.tolist()[0][1:]
        writer.goto(goto_cord)
        Current_score+=1
        writer.write(cord.values.tolist()[0][0])
        scorecard()
    else:
        print("not a state")

def scorecard():
    score.clear()
    score.write(f"Score: {Current_score}")






#screen.exitonclick()
screen.mainloop()