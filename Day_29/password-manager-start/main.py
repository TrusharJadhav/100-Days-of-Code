from tkinter import *
from tkinter import messagebox
import pyperclip
import string
import random
import pandas as pd
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
PASSWORD_LENGTH=16
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters=list(string.ascii_letters+string.digits+string.punctuation)
def generate_password():
    password_key =random.sample(letters,PASSWORD_LENGTH)
    password_key="".join(password_key)
    print(password_key)
    password.delete(0,END)
    password.insert(0,password_key)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_save=website.get()
    username_save=email.get()
    password_save=password.get()
    pyperclip.copy(password_save)
    if len(website_save)==0 or len(password_save)==0:
        print("Hi")
        messagebox.showinfo(title="Opps",message="Please enter website & password")
    #   
    else:
        save={"Website":website_save,"Username":username_save,"Password":password_save}
        is_ok=messagebox.askokcancel(title="Confirmation",message=f"You have entered \nWebsite:{website_save}\nEmail:{username_save}\nPassword:{password_save}\nIs it ok to Save?")
        if is_ok:
            with open("password.txt","a") as file:
                file.write(f"{website_save} | {username_save} | {password_save}\n")
            website.delete(0,END)
            password.delete(0,END)

    



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("My Password Manager")
window.config(padx=20,pady=20,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image_logo=PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=image_logo)
canvas.grid(row=0,column=1)

web=Label(text="Website")
web.grid(row=1,column=0)
website = Entry(width=40)
website.focus()
website.insert(END, string="")
website.grid(row=1,column=1,columnspan=2)


email_label=Label(text="Email")
email_label.grid(row=2,column=0)
email = Entry(width=40)
email.insert(END, string="jadhavtrushar@gmail.com")
email.grid(row=2,column=1,columnspan=2)


pass_label=Label(text="Password")
pass_label.grid(row=3,column=0)
password = Entry(width=25)
password.insert(END, string="")
password.grid(row=3,column=1)
pass_button=Button(text="Generate Password",command=generate_password)
pass_button.config(width=10)
pass_button.grid(row=3,column=2)

add_button=Button(text="Add",command=save)
add_button.config(width=25)
add_button.grid(row=4,column=1,columnspan=2)





window.mainloop()