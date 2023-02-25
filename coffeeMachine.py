#declaring coin vairiables and setting them to 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0
total = 0
#prompting the users for how many coins they have and re-assigning the coins variables
def changePrompt():
    global quarters, dimes, nickels, pennies
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

#calculating all of the coins and returning the values
def totalChange(coins):
    global quarters, dimes, nickels, pennies
    quarters =  quarters * coins["Quarter"]
    dimes = dimes * coins["Dime"]
    nickels = nickels * coins["Nickel"]
    pennies = pennies * coins["Penny"]
    total = quarters + dimes + nickels + pennies
    return total
##calculating the change to give back to the person    
def calCulateYourChange(coffee, index, totalchange):
        if totalchange <  coffee[index]["price"]:
            print("Sorry, that is not enough money. Money refunded")
        elif totalchange > coffee[index]["price"]:
            yourChange = totalchange - coffee[index]["price"]
            print(f"Here is ${yourChange:.2f} in change")
            print(f"Here is your {coffee[index]['Name']}")
            updateCoffeeMachine(coffeeMachine, coffee, index, total)    

#updating the coffee machine after the purchase
def updateCoffeeMachine(coffeeMachine, coffee ,index):
    coffeeMachine["Water"] -=  coffee[index]["Water"]  
    coffeeMachine["coffee"] -=  coffee[index]["coffee"] 
    coffeeMachine["Milk"] -=  coffee[index]["Milk"]
    coffeeMachine["Money"] += coffee[index]["price"]
#calculating if we have enough supplies. If we dont, informing the user that we dont have the supplies
def printNotEnoughMessage(index):
    #creating a loop to make it easier to get the indexes for the coffee dictionary
    for cof in coffee:
        waterDifference = coffeeMachine["Water"] - cof["Water"]
        milkDifference = coffeeMachine["Milk"] - coffee[1]["Milk"]
        coffeeDifference  = coffeeMachine["Water"] - cof["coffee"]
    if waterDifference <= 0:
        print(f"Sorry their is not enough water")
    elif milkDifference <= 0:
        print(f"Sorry their is not enough milk")
    elif coffeeDifference <= 0:
        print(f"Sorry their is not enough coffee")
    else:
        # if coffee, milk, and water is not less than 0, i will call the changeprompt and calculateyourchange function
        changePrompt()
        calCulateYourChange(coffee, index, totalChange(coins))
#creating dictionary of coffee that includes name, water, milk, coffee, and the price
coffee = [{"Name":"Expresso", "Water": 50, "Milk":0, "coffee":18, "price":1.50}, 
        {"Name":"Latte", "Water": 200, "coffee":24 ,"Milk":150, "price":2.50},
         {"Name":"Cappuccino", "Water": 250, "coffee":24 ,"Milk":100, "price": 3.00}]
#creating dictionary of the the coffeemachine
coffeeMachine ={"Water":300, "Milk":200,"coffee": 100, "Money": 0} 
#creating coins dictionary
coins = {"Penny": .01, "Nickel": .05, "Dime":.10, "Quarter":.25}
#creating infinite loop so the game never ends
while True:    
    #prompting the user on what type of drink they want
    coffeeChoise = input("What would you like? (expresso/latte/cappuccino): ")
    if coffeeChoise.lower() == "report":
        #printing off the report
        for supplyKey, supplyValue  in coffeeMachine.items():
            print(f"{supplyKey}: {supplyValue}")
            #calling the main function and inputting the index
    elif  coffeeChoise.lower() == "latte":
        printNotEnoughMessage(1)
    elif  coffeeChoise.lower() == "expresso":
        printNotEnoughMessage(0)
    elif  coffeeChoise.lower() == "cappuccino":
       printNotEnoughMessage(2)