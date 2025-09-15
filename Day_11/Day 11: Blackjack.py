import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
Your_Score=0
Computer_Score=0
def score(hand):
    Score=0
    for card in hand:
        Score+=card
    if 11 in hand and Score>21:
        Score-=10
    return Score
    


random.shuffle(cards)
Your_hand=cards[0:2]
Computer_hand=cards[2:4]

print(f"Your Hand is: {Your_hand}")
print(f"Your score {score(Your_hand)}")
print(f"Computer Hand is: {Computer_hand[0]} & Hidden")
#
choice=input("Hit or Stand  ").lower()
if choice=="hit":
    random.shuffle(cards)
    Your_hand.append(cards[0])
    print(f"Your Hand is: {Your_hand}")
    print(f"Your score {score(Your_hand)}")

random.shuffle(cards)
Computer_hand.append(cards[0])
Computer_Score=score(Computer_hand)
Your_Score=score(Your_hand)



if Your_Score>21:
    print("You are busted")
elif Computer_Score>21:
    print("You won, Computer busted")
else:
    if Computer_Score>Your_Score:
        print("Computer won")
    elif Computer_Score==Your_Score:
        print("Its Tie")
    else:
        print("You won")



