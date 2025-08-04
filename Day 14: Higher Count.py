
from art import *

print(text2art("HIGHER LOWER"))
from Day_14_game_data import data
import random
score=0
game_over=True
A=random.choice(data)

while game_over==True:
    B=random.choice(data)
    print("-+"*50)
    print(f"Compare A: {A["name"]}, {A["description"]},{A["country"]}")
    print(text2art("Vs"))
    print(f"Compare B: {B["name"]}, {B["description"]},{B["country"]}")
    print("-+"*50)
    if A["follower_count"]>B["follower_count"]:
        Winner="A"
    else:
        Winner="B"
        A=B
  
    choice=input("Who has more followers 'A' or 'B' ?")

    if choice==Winner:
        score+=1
        
    else:
        game_over=False

    print(f"Followers count of A: {A["follower_count"]}")
    print(f"Followers count of B: {B["follower_count"]}")
    print("Your score: " + str(score))
