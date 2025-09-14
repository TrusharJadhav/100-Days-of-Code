from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    counter(5)

def counter(count):
    print(count)
    canvas.itemconfig(timer_text,text=count)
    while count>0:
        window.after(1000,counter,count-1)
def reset_timer():
    print("Timer Stopped")


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomoto_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomoto_img)
canvas.grid(row=1,column=1)




label_tick=Label(text="✅",fg=GREEN,bg=YELLOW,font=("Aerial",18,"bold"))
label_tick.grid(row=2,column=1)


label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=("Aerial",48,"bold"))
label.grid(row=0,column=1)

timer_text=canvas.create_text(100,130,text="0:00",fill="white",font=("Aeriel",24,"bold"))
canvas.grid(row=1,column=1)

start=Button(text="Start",font=("Aeriel",24,"bold"),fg=GREEN,bg=YELLOW,highlightthickness=0,command=start_timer)
start.grid(row=2,column=0)

reset=Button(text="Reset",font=("Aeriel",24,"bold"),fg=GREEN,bg=YELLOW,highlightthickness=0,command=reset_timer)
reset.grid(row=2,column=2)





window.mainloop()