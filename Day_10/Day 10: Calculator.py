from art import *
print(text2art("CALC"))


def operation(a,b,ops):
    if ops=="/":
        c=a/b
    elif ops=="*":
        c=a*b
    elif ops=="+":
        c=a+b
    elif ops=="-":
        c=a-b
    return c


a=float(input("Enter First number: "))

def calculator(a):
    ops=input("What Operation you want to perform Select \n* \n/ \n+ \n-  :    ")
    b=float(input("Enter second number: "))
    ans=operation(a,b,ops)
    print(f"{a}{ops}{b} = {ans}")
    return ans
ans= calculator(a)
should_continue="y"

while should_continue=="y"or should_continue=="n":
    should_continue = input(f"Do you want to continue operation with {ans} \n Select 'y' for contnue, \n Select 'n' to start new operation, \n Select any key to exit ")
    if should_continue=="y":
        ans=calculator(ans)
    elif should_continue=="n":
        a=float(input("Enter First number: "))
        ans=calculator(a)
    else:
        print("*"*30+" THANKS FOR USING CALCULATOR "+"*"*30)
        exit()
    

