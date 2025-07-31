import string

alphabets=[]
str=string.ascii_lowercase
for letter in str:
    alphabets.append(letter)

def encrypt(message,shift,direction):
    Scrambled_Message=""
    if direction=="encrypt":
        shift=shift
    elif direction=="decrypt":
        shift=-1*shift
    for letter in message:
        if letter not in alphabets:
            Scrambled_Message+=letter
        else:
            id=alphabets.index(letter)
            delta=(id+shift)%26
            Scrambled_Message+=alphabets[delta]
    return Scrambled_Message


message=input("Type your Message: ").lower()
shift=int(input("Enter shift by how many letters: "))
direction=input("Do you want to Encrypt or Decrypt: ").lower()


print(message)
scrambled_message=encrypt(message,shift,direction)
print(scrambled_message)
