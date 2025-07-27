import random
Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


'''
Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
Game_Image={"Rock":Rock,"Paper":Paper,"Scissor":Scissor}
Player_Choice=input("What you want to choose, Rock, Papaer or Scissor ")
Computer_Choice=random.choice(["Rock","Paper","Scissor"])
print("You Choose:")
print(Game_Image[Player_Choice])
print("Computer Choose:")
print(Game_Image[Computer_Choice])

if Player_Choice==Computer_Choice:
    print("It's Tie")
elif Player_Choice=="Rock" and Computer_Choice=="Scissor":
    print("You win")
    if Player_Choice=="Rock" and Computer_Choice=="Paper":
        print("Computer Win")
elif Player_Choice=="Paper" and Computer_Choice=="Rock":
    print("You win")
    if Player_Choice=="Paper" and Computer_Choice=="Scissor":
        print("Computer Win")
elif Player_Choice=="Scissor" and Computer_Choice=="Rock":
    print("Computer win")
    if Player_Choice=="Scissor" and Computer_Choice=="Paper":
        print("You Win")  




