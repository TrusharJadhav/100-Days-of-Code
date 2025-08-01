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

should_continue="y"
ans=0
while should_continue=="y" or should_continue=="n":
    if should_continue=="n":
        a=float(input("Enter First number: "))
        ops=input("What Operation you want to perform Select \n* \n/ \n+ \n- \n")
        b=float(input("Enter second number: "))
        ans=operation(a,b,ops)
        print(f"{a}{ops}{b} = {ans}")
        should_continue=input(f"Do you want to continue operation with {ans} \n Select 'y' for contnue, \n Select 'n' to start new operation ")
    elif should_continue=="y":
        pass
