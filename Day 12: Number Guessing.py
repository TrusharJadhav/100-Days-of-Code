from art import *
import random
print("Number Guessing Grouping")
diff_level=str(input("Chosse Difficulty Level,'Easy' or 'Hard'").lower())
print("Guess Number between 1 & 100")

if diff_level=="hard":
    Max_guesses= 5
elif diff_level=="easy":
    Max_guesses= 10
print(f"You have {Max_guesses} guesses to predict number")
counter=0
Number=random.choice(range(1,100))

while counter<=Max_guesses:
    guess=int(input("What is your Guess: "))
    if guess<=.5* Number:
        print("Too low")
    elif guess<Number:
        print("Low")
    elif guess>2*Number:
        print("Too High")
    elif guess>Number:
        print("High")
    elif guess==Number:
        print("Bang on, your guess right answer, Number is {Number}") 
        break
    counter+=1