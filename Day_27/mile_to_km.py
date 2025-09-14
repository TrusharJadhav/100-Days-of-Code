from tkinter import *
window=Tk()
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)
window.title("Miles to KM Convertor")


miles=Entry()
miles.grid(column=1,row=0)
mile_label=Label(text="Miles")
mile_label.grid(column=2,row=0)
is_equal=Label(text="is equal to")
is_equal.grid(column=0,row=1)

km_result_label=Label(text=0)
km_result_label.grid(column=1,row=1)
km_label=Label(text="km")
km_label.grid(column=2,row=1)
def cal():
    km=int(miles.get())*8/5
    km_result_label.config(text=km)

calculator_button=Button(text="Calculate",command=cal)
calculator_button.grid(column=1,row=2)

mainloop()

