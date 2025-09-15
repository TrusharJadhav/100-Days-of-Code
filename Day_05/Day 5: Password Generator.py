import random
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to Password Generators")
Num_Letters=int(input("How many letters you want to include in Password: "))
Num_Numbers=int(input("How many NUmbers you want to include in Password: "))
Num_Symbols=int(input("How many Symbols you want to include in Password: "))

random.shuffle(Letters)
random.shuffle(Numbers)
random.shuffle(Symbols)
Simple_Password=Letters[0:Num_Letters]+ Numbers[0:Num_Numbers]+ Symbols[0:Num_Symbols]

random.shuffle(Simple_Password)
Password=""
for item in Simple_Password:
    Password+=item
print(Password)