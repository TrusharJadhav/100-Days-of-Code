with open("./Input/Letters/starting_letter.txt","r") as content_draft:
    draft=content_draft.readlines()
with open("./Input/Names/invited_names.txt","r") as content_names:
    invitees=content_names.readlines()
print(invitees)
for invitee in invitees:
    draft[0]=f"Dear {invitee},"
    text_block="\n".join(draft)
    letter=f"letter for {invitee}.txt"
    with open(f"./Output/{letter}","w") as invitation:
        invitation.write(text_block)


