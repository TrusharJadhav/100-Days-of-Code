
import datetime
def life_in_weeks(date):
    print(date)

#birthdate=input("What is your birthdate(YYYY-MM-DD)")
birthdate=datetime.datetime(1990,1,12)
#birthdate=datetime.strptime(birthdate,"%Y-%m-%d")
age=(datetime.datetime.today() - birthdate)
Age=age.days//7
Time=90*52-Age
print(f"You have {Time} weeks left")