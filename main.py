from buy import selectBuys
from stock import stockManager

# Introduction
print("Welcome to money manager simulator")
print("Congrats, Your financial troubles are now over, \
with this program you will be able to find out if \
you will be able to support your current lifestyle \
based on your yearly income.")


def askCosts(questions):
    """ Ask the user a bunch of questions to determine their yearly or one time costs. """
    totalCost = 0
    # ask questions
    for q in questions:
        currCost = int(input(q))
        totalCost += currCost
    # additional costs
    print("Enter any additional costs (NA to quit). Write the item then the cost in dollars.")
    inputStr = "ITEM 0"
    while inputStr != "NA":
        item, currCost = inputStr.split(' ')
        totalCost += int(currCost)
        inputStr = input("Enter additional costs: ")
    # return the total costs
    return totalCost


def askWants(questions):
    """ Ask the user a bunch of questions to determine their yearly or one time wants. """
    itemNames = []
    prices = []
    values = []
    print("Respond in the form: \"itemName price happinessValue\". If there is no answer enter NA")
    # ask questions
    for q in questions:
        inputStr = input(q)
        if inputStr != "NA":
            itemName, price, value = inputStr.split(' ')
            itemNames.append(itemName)
            prices.append(int(price))
            values.append(int(value))
    # additional wants
    print("Enter any additional wants with the same format as before (NA to quit).")
    inputStr = input("Enter additional costs:")
    while inputStr != "NA":
        itemName, price, value = inputStr.split(' ')
        itemNames.append(itemName)
        prices.append(int(price))
        values.append(int(value))
        inputStr = input("Enter additional costs:")
    # return the names, prices, and values
    return itemNames, prices, values


# get the net salary (income - taxes)
income = int(input("Enter your income per year: "))
taxes = 0
if income >= 625370:
    taxes += 60789.92+((income-625369)*0.123)
elif income >= 375222:
    taxes += 32523.20+((income-375221)*0.113)
elif income >= 312687:
    taxes += 26082.09+((income-312687)*0.103)
elif income >= 61215:
    taxes += 2695.19+((income-61215)*0.093)
elif income >= 48436:
    taxes += 1672.87+((income-48436)*0.08)
elif income >= 34893:
    taxes += 860.29+((income-34893)*0.06)
elif income >= 22108:
    taxes += 348.89+((income-22108)*0.04)
elif income >= 9326:
    taxes += 93.25+((income-9326)*0.02)
else:
    taxes = income*0.01
income = income-taxes

# yearly costs
print("Please enter your yearly cost for the following items (in USD)")
yearlyCosts = askCosts(
    ["Rent/Mortgage: ", "Food: ", "Gas: ", "Electricity bill: "])
yearlyBudget = income-yearlyCosts
print(yearlyBudget)
if(yearlyBudget < 0):
    print("insufficient funds")
    exit()
else:
    print("This is how much you can spend/ have savings per year", yearlyBudget)

# yearly wants
yearlyWantsPrices = []
yearlyWantsValues = []
yearlyWants = [str]
# WRITE THIS LATER

# Major loop (1 iteration = 1 year)
yearsToSimulate = int(input("How many years do you want to simulate: "))
yearlyLeftOver = 0
trading = stockManager()
for year in range(yearsToSimulate):
    # one time costs
    currBudget = yearlyBudget + yearlyLeftOver
    currBudget -= askCosts(["Did you have any medical expenses"],
                           ["Do you want to go on a vacation if so how much did it cost"],
                           ["Did you donate any money"],
                           ["How much money did you spend on your hobbies"],
                           ["Do you owe any money this year?"])

    # stocks
    print("These are the stocks you have:")
    trading.display()
    inputStr = input("Would you like to trade stocks (y/N): ")
    while lower(inputStr[0]) != 'n':
        ticker, shares, action = input(
            "Enter the ticker, # of shares, and buy or sell: ")
        if action == "buy":
            currBudget -= trading.buy(ticker, int(shares))
        elif action == "sell":
            currBudget += trading.sell(ticker, int(shares))
        else:
            print("invalid action")
        inputStr = input("Would you like to continue trading stocks (y/N): ")

    # one time wants
    print("You can spend $", currBudget, "this year on things you want")
    oneTimeWantsPrices = []
    oneTimeWantsValues = []
    oneTimeWants = [str]
    # WRITE THIS LATER

    # "buy the items"
    yearlyPurchases, oneTimePurchases, happiness, amountSpent = selectBuys(
        currBudget, yearlyWantsPrices, yearlyWantsValues, oneTimeWantsValues, oneTimeWantsValues)
    yearlyLeftOver = currBudget - amountSpent
    print("BUY THE FOLLOWING YEARLY ITEMS")
    for i in yearlyPurchases:
        print(yearlyWants[i])
    print("BUY THE FOLLOWING ONE TIME PURCHASES")
    for i in oneTimePurchases:
        print(oneTimeWants[i])


# ending
print("Thank you for playing the money manager simulator")
