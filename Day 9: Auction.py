logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
should_continue="yes"
bids={}
while should_continue=="yes":
    name=input("What is your name: ")
    Bid=int(input("What is your Bid: $ "))
    bids[name]=Bid
    should_continue=input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    print("\n"*20)
max=0
winner=""
for key in bids:
    if max<bids[key]:
        max=bids[key]
        winner=key
# print(bids)
# max(bids,key=bids.get)
print(f"Winner of the Auction is {winner} ")


