import random
words=["Apple1","Mango","Coffee23"]
word=random.choice(words)
print(" - "*len(word))
correct_letter=[]

lives=0
while lives<=6:
    New_guess=""
    guess=input("Guess a letter: ")
    for letter in word:
        if guess==letter:
            New_guess+=guess
            correct_letter.append(guess)
        elif letter in correct_letter:
            New_guess+=letter
        else:
            New_guess+= " _ "
    print(New_guess)
    lives+=1
   

