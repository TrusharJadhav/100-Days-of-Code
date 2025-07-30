import string
message=input("Type your Message: ").lower()
scramble=int(input("Enter shift by how many letters: "))
alphabets=[]
str=string.ascii_lowercase
for letter in str:
    alphabets.append(letter)

Scrambled=alphabets[scramble:]+alphabets[:scramble]
Scrambled_Message=""

for letter in message:
    if letter==" ":
        Scrambled_Message+=" "
    else:
        id=alphabets.index(letter)
        Scrambled_Message+=Scrambled[id]
print(Scrambled_Message)