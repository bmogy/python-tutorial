import random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerHand = []
dealerHand = []
gameOn = True

# grabs a random number from the list
def drawCard():
    randomCard = random.randint(0, len(deck) -1)
    return deck[randomCard]
def playerdrawCard():
    playerHand.append(drawCard())
def  dealerDrawCard():
    dealerHand.append(drawCard())
def firstHand():
    for _ in range(2):
        playerdrawCard()
        dealerDrawCard()
def getScore(playerOrDealer):
    Score = 0  
    for hand in playerOrDealer:
        Score += hand
    if 11 in playerOrDealer and Score > 21:
        playerOrDealer.remove(11)
        playerOrDealer.append(1)
        for hand in playerOrDealer:
            Score += hand
        return Score
    else:
        return Score
def printPlayerandDeallerScore():
    print(f"Your cards:{playerHand}, current score: {getScore(playerHand)}")
    print(f"Computers first card: {dealerHand[0]}")
def finalMessage():
    print(f"Your final hand: {playerHand}, final score: {getScore(playerHand)}")
    print(f"Computers final hand: {dealerHand} final score: {getScore(dealerHand)}")
    if getScore(dealerHand) > 21 and getScore(playerHand) > 21:
         print("Both Dealer and player went over, you both lose")
    elif getScore(playerHand) <= 21 and getScore(dealerHand) > 21:
        print("The dealer bust and went over 21, player 1 wins")
    elif getScore(dealerHand) <= 21 and getScore(playerHand) > 21:
        print("The player bust and went over 21. Dealer 1 wins")
    elif getScore(dealerHand) > getScore(playerHand):
        print("The dealer wins the game")
    elif getScore(dealerHand) < getScore(playerHand):
        print("Woohoo, you win the  game")
    elif getScore(playerHand) > 21:
        print("You went over you lose")
    elif getScore(dealerHand) == getScore(playerHand):
        print("It is a draw, you both have the same score")
def dealerDrawCard():
    if getScore(dealerHand) < 16:
        dealerHand.append(drawCard())         
def getCardOrPassMethod():
        getCardOrPass = input("Type 'y' to get another card, type 'n' to pass: ")
        if getCardOrPass.lower() == "y":
            playerdrawCard()
            printPlayerandDeallerScore()
            if getScore(playerHand) < 21:
                getCardOrPassMethod()
            else:
                finalMessage()

        elif getCardOrPass.lower() =="n":
            finalMessage()
while gameOn:
    playGame = input("Do you want to play a game of Black jack? type 'y' or 'n': ")
    if playGame == "y":
        playerHand =[]
        dealerHand = []
        firstHand()
        print(getScore(playerHand))
        printPlayerandDeallerScore()
        dealerDrawCard()
        getCardOrPassMethod()
    elif playGame == "n":
        gameOn = False
    
        