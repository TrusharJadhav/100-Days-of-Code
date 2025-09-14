# def add(*input):
#     for i in input:
#         print(i)

# add(1,2,3,4,5,5)
from tkinter import *
window=Tk()
window.minsize(width=400,height=400)
window.title("Miles to KM convertor")


#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Please Enter distance in miles.")
#Gets text in entry
print(entry.get())
entry.pack()
#Labels
label = Label(text="Distance in km:")

label.pack()


def action():
    km=int(entry.get())*8/5
    label.config(text=km)




#calls action() when pressed
button = Button(text="Calculate", command=action)
button.pack()

mainloop()