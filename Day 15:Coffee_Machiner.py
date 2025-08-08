MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#Check resources
def check_resources(choice):
    if choice=="report":
        Avail_Resources=resources
    else:
        ingredients=MENU[choice]["ingredients"]
        Avail_Resources=resources
        for k in ingredients:
            Avail_Resources[k]=Avail_Resources[k]-ingredients[k]
            if Avail_Resources[k]<0:
                print(f"Sorry, We do not have enough {k}.")
                exit()
    return Avail_Resources

def check_transcation(choice,earning):
    quarter=int(input("How Many Quarters? "))
    dime=int(input("How many dimes? "))
    nickle=int(input("How many nickles? "))
    penny=int(input("How many penny? "))
    paid=.25*quarter+.1*dime+.05*nickle+.01*penny
    change=round(paid-MENU[choice]["cost"],2)
    if change <0:
        print("Sorry that's not enough money. Money refunded.")
    elif change==0:
        print("You put in the exact amount needed!")
    else:
        print(f"Transction Succesfull. You have paid {paid}, here is your change {change}\n Here is your {choice} ☕️ \nEnjoy Your Coffee.")
    earning=earning+MENU[choice]["cost"]
    return earning
def report():
    if earning==0:
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    else:
        print(f"Water: {Avail_Resources['water']}ml")
        print(f"Milk: {Avail_Resources['milk']}ml")
        print(f"Coffee: {Avail_Resources['coffee']}g")
    print(f"Total Earning are: {earning}")
Machine_status= True
earning=0
while Machine_status==True:
    choice=input("What would you like 'Espresso/Latte/Cappucciano: ").lower()
    print(f"You have selected {choice}!")
    if choice=="off":
        exit()
    if choice=="report":
        report()
    else:
        Avail_Resources=check_resources(choice)
        earning=check_transcation(choice,earning)
        

