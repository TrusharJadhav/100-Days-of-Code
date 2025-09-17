# constants
from tkinter import *
from tkinter import messagebox
import pyperclip
import string
import random
import json
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
    new_data={
        website_save:{
            "email":username_save,
            "password":password_save
        }
    }
    if len(website_save)==0 or len(password_save)==0:
        print("Hi")
        messagebox.showinfo(title="Opps",message="Please enter website & password")
    #   
    else:
        save={"Website":website_save,"Username":username_save,"Password":password_save}
        is_ok=messagebox.askokcancel(title="Confirmation",message=f"You have entered \nWebsite:{website_save}\nEmail:{username_save}\nPassword:{password_save}\nIs it ok to Save?")
        if is_ok:
            
            try:
                with open("password.json","r") as file:
                    data=json.load(file)
            except FileNotFoundError:
               with open("password.json","w") as file:
                    json.dump(new_data,file,indent=4)
            else:    
                data.update(new_data)
                with open("password.json","w") as file:
                    json.dump(data,file,indent=4)
            finally:
                # file.write(f"{website_save} | {username_save} | {password_save}\n")
                website.delete(0,END)
                password.delete(0,END)

# ---------------------------- SEARCH ------------------------------- #    
def search():
    with open("password.json","r") as file:
        data=json.load(file)
        search_key=website.get()
        if search_key in data:
            email_key=data[search_key]["email"]
            password_key=data[search_key]["password"]
            email.delete(0,END)
            email.insert(0, string=email_key)
            password.insert(0,string=password_key)
            messagebox.showinfo(title=search_key,message=f"{search_key}\nEmail:{email_key}\nPassword:{password_key}")
        else:
            messagebox.showinfo(title="Opps",message="No details Found")

          
    


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
website = Entry(width=25)
website.focus()
website.insert(0, string="")
website.grid(row=1,column=1,columnspan=1)


email_label=Label(text="Email")
email_label.grid(row=2,column=0)
email = Entry(width=40)
email.insert(0, string="jadhavtrushar@gmail.com")
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

search_button=Button(text="Search",command=search)
search_button.config(width=10)
search_button.grid(row=1,column=2,columnspan=1)





window.mainloop()