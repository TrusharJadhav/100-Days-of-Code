from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Machine=CoffeeMaker()
Menu=Menu()
Money_Machine=MoneyMachine()


machine_is_on=True
while machine_is_on==True:
    choice=input(f"What you would like to have {Menu.get_items()}: ").lower()
    drink=Menu.find_drink(choice)
    if choice=="report":
        Money_Machine.report()
        Machine.report()
    elif choice=="off":
        machine_is_on=False
    else:
        if Machine.is_resource_sufficient(drink)==True:
            drink=Menu.find_drink(choice)
            if Money_Machine.make_payment(drink.cost):
                Machine.make_coffee(drink)
        else:
            print("Insufficient resources")
            machine_is_on=False

