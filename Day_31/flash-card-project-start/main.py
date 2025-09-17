BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

#------------UI SETUP----------------------
window=Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=626,bg=BACKGROUND_COLOR,highlightthickness=0)

front=PhotoImage(file="./images/card_front.png")
back=PhotoImage(file="./images/card_back.png")
right=PhotoImage(file="./images/right.png")
wrong=PhotoImage(file="./images/wrong.png")



canvas.create_image(400,263,image=front)
canvas.grid(row=0,column=0,columnspan=2)
canvas.create_image(250,575,image=right)
canvas.grid(row=1,column=0,columnspan=1)
canvas.create_image(550,575,image=wrong)
canvas.grid(row=1,column=1,columnspan=1)

french=Label(text="French",font=("Aerial",40,"Italic"))


window.mainloop()
#------------SETUP----------------------