import datetime as dt
import smtplib
import pandas as pd

data=pd.read_csv("birthdates.csv")

now=dt.datetime.now()
month=now.month
day=now.day

today_bday=data[(data["month"]==month) & (data["day"]==day)]

name=today_bday.name.values[0]

subject="Happy Birthday"
body=f"Dear {name},\nWish you many many happy returns of the day\nRegards,\nTrushar"
message=f"Subject:{subject}\n\n{body}"


with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    user="jadhavtrushar@gmail.com"
    password=""    
    connection.login(user=user,password=password)

    connection.sendmail(from_addr=user,to_addrs="drshilpakumbhar@gmail.com",msg=message)

# with smtplib.SMTP("smtp.gmail.com",port=587) as smtp:
#     smtp.starttls()
#     smtp.login(user=email,password=password)
#     subject="Motivational Quote"
#     body=quote
#     message=f"Subject:{subject}\n\n{body}"
#     smtp.sendmail(email,"drshilpakumbhar@gmail.com",message)