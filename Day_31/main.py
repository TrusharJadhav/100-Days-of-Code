from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
#------------UI SETUP----------------------
window=Tk()
window.title("Flash Card App")
window.config(padx=0,pady=0,bg=YELLOW)


canvas=Canvas(width=600,height=400,bg=YELLOW,highlightthickness=0)

canvas.create_rectangle(50,50,500,250,fill="white",radius=30)



canvas.pack()
#------------SETUP----------------------




window.mainloop()