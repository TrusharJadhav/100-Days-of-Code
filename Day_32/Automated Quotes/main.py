import smtplib
import random
import datetime as dt
email="jadhavtrushar@gmail.com"
password=""
data=[]
with open("quotes.txt","r") as file:
    data=file.readlines()
    quote = random.choice(data)

now=dt.datetime.now()
if now.weekday()==0:
    with smtplib.SMTP("smtp.gmail.com",port=587) as smtp:
        smtp.starttls()
        smtp.login(user=email,password=password)
        subject="Motivational Quote"
        body=quote
        message=f"Subject:{subject}\n\n{body}"
        smtp.sendmail(email,"drshilpakumbhar@gmail.com",message)

    