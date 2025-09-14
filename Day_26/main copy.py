from turtle import Turtle, Screen
import pandas as pd
import time
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
def scorecard():
    score.clear()
    score.write(f"Score: {Current_score}",align="center",font=("Arial",24,"normal"))
All_states=states.state.values.tolist()
states_to_learn=All_states
game_is_on=True
while game_is_on:
    answer=screen.textinput(title="Guess the State", prompt="What's another state name")

    if answer in All_states:
        cord=states[states["state"]==answer]
        states_to_learn.remove(answer)
        goto_cord=cord.values.tolist()[0][1:]
        writer.goto(goto_cord)
        Current_score+=1
        writer.write(cord.values.tolist()[0][0],align="center",font=("Arial",16,"normal"))
        scorecard()
    elif answer=="exit":
        print(f"You need to learn below statess:\n{states_to_learn}")
        for state in states_to_learn:
            cord=states[states["state"]==state]
            goto_cord=cord.values.tolist()[0][1:]
            writer.goto(goto_cord)
            writer.write(cord.values.tolist()[0][0],align="center",font=("Arial",16,"normal"))
        time.sleep(5)
        exit()
    else:
        print("not a state")



#screen.exitonclick()
screen.mainloop()