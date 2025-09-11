PLACEHOLDER="[name]"
with open("./Input/Letters/starting_letter.txt","r") as content_draft:
    draft=content_draft.read()
with open("./Input/Names/invited_names.txt","r") as content_names:
    invitees=content_names.readlines()

for invitee in invitees:
    stripped=invitee=invitee.strip()
    invitation= draft.replace(PLACEHOLDER,invitee)
    print(invitation)
    with open(f"./Output/ReadyToSend/letter_for_ {invitee}.txt","w") as completed_letter:
       completed_letter.write(invitation)


