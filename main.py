from buy import selectBuys

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
    item = ""
    currCost = 0
    while item != "NA":
        totalCost += currCost
        item, currCost = input("Enter additional costs: ").split(' ')
    # return the total costs
    return totalCost


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
for year in range(yearsToSimulate):
    currBudget = yearlyBudget + yearlyLeftOver
    # one time costs
    currBudget -= askCosts(["Did you have any medical expenses"])
    # ASK MORE QUESTIONS

    # one time wants
    # WRITE THIS LATER
    oneTimeWantsPrices = []
    oneTimeWantsValues = []
    oneTimeWants = [str]
    # price + happiness

    # "buy the items"
    yearlyPurchases, oneTimePurchases, happiness, amountSpent = selectBuys(
        currBudget, yearlyWantsPrices, yearlyWantsValues, oneTimeWantsValues, oneTimeWantsValues)
    yearlyLeftOver = currBudget - amountSpent
    for i in yearlyPurchases:
        print(yearlyWants[i])
    # PRINT THE ITEMS THAT WERE BOUGHT

    # STOCKS

# ending
print("Thank you for playing the money manager simulator")
