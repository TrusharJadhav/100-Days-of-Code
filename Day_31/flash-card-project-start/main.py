BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random
import time
#-----------------Dictionary---------------------------------
try:
    data=pd.read_csv("./data/to_learn.csv")
    to_learn=data.to_dict(orient="records")

except:
    data=pd.read_csv("./data/french_words.csv")
    to_learn=data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(canvas_image,image=front)
    french=current_card["French"]
    
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(question,text=french,fill="black")
    flip_timer=window.after(3000,func=flip_card)
    

def flip_card():
    global current_card
    canvas.itemconfig(canvas_image,image=back)
    canvas.itemconfig(card_title,text="English",fill="white")
    english=current_card["English"]
    canvas.itemconfig(question,text=english,fill="white")
    
    
def is_known():
    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("./data/to_learn.csv",index=False)
    print(len(to_learn))

    next_card()
#-----------------UI SETUP---------------------------------

window=Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
flip_timer=window.after(3000,func=flip_card)


front=PhotoImage(file="./images/card_front.png")
back=PhotoImage(file="./images/card_back.png")




canvas_image=canvas.create_image(400,263,image=front)
card_title=canvas.create_text(400,150,text="French",font=("Aerial",40,"italic"))
question=canvas.create_text(400,263,text="word",font=("Aerial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

right=PhotoImage(file="./images/right.png")
known=Button(image=right,highlightthickness=0,command=is_known)
known.grid(row=1,column=0)

wrong=PhotoImage(file="./images/wrong.png")
unknown=Button(image=wrong,highlightthickness=0,command=next_card)
unknown.grid(row=1,column=1)

next_card()

window.mainloop()
#------------SETUP----------------------
