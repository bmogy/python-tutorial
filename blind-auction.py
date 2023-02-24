import os
print("Welcome to the auction program")
people_name_bid = []
gameStart = True
while gameStart:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    def collectNamesandBids(personName, personBid):
        people_name_bid.append({"Name":personName, "Bid":personBid})
    collectNamesandBids(name,bid)
    otherBidders = input("Are there any other bidders? Type 'yes' or 'no'")
    if otherBidders.lower() == "no":
        gameStart = False
    elif otherBidders.lower() == "yes":
        os.system('cls')
        gameStart = True
maxPrice = max(people_name_bid, key=lambda x:x['Bid'])
print("The winner is " + maxPrice["Name"] + " and the total bis was " + str(maxPrice["Bid"]))
    
    






