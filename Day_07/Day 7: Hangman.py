import random
words=["Apple1","Mango","Coffee23"]
word=random.choice(words).lower()
print(" - "*len(word))
correct_letter=[]

print("Welcome to Hangman")
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
      ''')

stages=[
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

lives=6
game_over=False
while game_over==False:
    
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
    
    if guess not in word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    
    print(New_guess)
    print(stages[6-lives])
    print("*"*15+"You have "+ str(lives)+ " of 6 lives left"+"*"*15)
    if lives==0:
        game_over=True
    
    if len(correct_letter)==len(word):
        print("You Won")
        game_over=True
print("Game Over")

