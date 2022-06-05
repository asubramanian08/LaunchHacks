from buy import selectBuys
from stocks import stockManager

# TODO main.py: add better comments
#   Docstring, whole files notes, arg type, return type
# TODO main.py: make more robust (handle all inputs)
# TODO all files: reformat + one line init + divide lines
# TODO: final run -> lots of testing


def askCosts() -> float:
    """ Determine the users yearly or one time costs. """
    totalCost = 0
    print("Write the item then the cost in dollars (NA to stop).")
    inputStr = input("Enter a cost: ")
    while inputStr.upper() != "NA":
        item, currCost = inputStr.split(' ')
        totalCost += round(float(currCost), 2)
        inputStr = input("Enter another cost: ")
    return totalCost


def askWants() -> (list, list, list):
    """ Determine the users yearly or one time wants. """
    itemNames = []
    prices = []
    values = []
    print("Respond in the form \"itemName price happinessValue\" (NA to stop).")
    inputStr = input("Enter a wanted item: ")
    while inputStr.upper() != "NA":
        itemName, price, value = inputStr.split(' ')
        itemNames.append(itemName)
        prices.append(round(float(price), 2))
        values.append(round(float(value), 2))
        inputStr = input("Enter another wanted item: ")
    return itemNames, prices, values


# Introduction
print()  # new line
print("Welcome to money manager simulator!")
print("Congrats! Your financial troubles are now over.")
print("Just try not to make your account go into the negatives. ")
print("With this program you will be better informed about your finances.")
yearsToSimulate = int(input("How many years do you want to simulate: "))
print()  # new line


# Net salary (income - taxes)
income = round(float(input("Enter your income per year: $")), 2)
taxes = 0
if income >= 625370:
    taxes += 60789.92 + ((income - 625369) * 0.123)
elif income >= 375222:
    taxes += 32523.20 + ((income - 375221) * 0.113)
elif income >= 312687:
    taxes += 26082.09 + ((income - 312687) * 0.103)
elif income >= 61215:
    taxes += 2695.19 + ((income - 61215) * 0.093)
elif income >= 48436:
    taxes += 1672.87 + ((income - 48436) * 0.08)
elif income >= 34893:
    taxes += 860.29 + ((income - 34893) * 0.06)
elif income >= 22108:
    taxes += 348.89 + ((income - 22108) * 0.04)
elif income >= 9326:
    taxes += 93.25 + ((income - 9326) * 0.02)
else:
    taxes = income * 0.01
income = income - taxes
taxes = round(taxes, 2)
income = round(income, 2)
print(f"You have ${taxes:.2f} of income taxes, \
leaving you with ${income:.2f} to spend.")
print()  # new line


# Yearly costs
print("Enter your yearly costs for the following items (in USD).")
print("Think about: Rent, Gas, Electricity, Long term goals, ...")
yearlyCosts = askCosts()
yearlyBudget = round(income - yearlyCosts, 2)
if (yearlyBudget < 0):
    exit("insufficient funds\n")
else:
    print(f"You can spend ${yearlyBudget:.2f} every year.")
print()  # new line


# Yearly wants
print("Enter the items you want ever year (in USD).")
print("Think about: 6 flags season pass, netflix, newspaper, ...")
yearlyWants, yearlyWantsPrices, yearlyWantsValues = askWants()
print()  # new line


# Major loop (1 iteration simulates 1 year)
yearlyLeftOver = 0
stockSimulator = stockManager()
print("Starting year by year simulation.\n")
for year in range(yearsToSimulate):
    # Inform user
    print(f"\nYear {year + 1}:")
    currBudget = yearlyBudget + yearlyLeftOver
    print(f"You can spend ${currBudget:.2f} in total this year")
    print()  # new line

    # One time costs
    print("Enter your costs for this year (in USD).")
    print("Think about: Medical costs, Vacation, Donations, ...")
    currBudget -= askCosts()
    print()  # new line

    # Stock trading
    print("These are the stocks you have.")
    stockSimulator.display()
    inputStr = input("Would you like to trade stocks (y/N): ")
    while inputStr[0].lower() != 'n':
        print(f"You have ${currBudget:.2f} left to spend.")
        action, ticker, shares = input(
            "Enter buy or sell, ticker, and # of shares: ").split(' ')
        if action == "buy":
            bought, price = stockSimulator.buy(ticker, int(shares), currBudget)
            print(f"Bought {bought} shares of {ticker} at ${price:.2f}.")
            currBudget -= bought * price
        elif action == "sell":
            sold, price = stockSimulator.sell(ticker, int(shares))
            print(f"Sold {sold} shares of {ticker} at ${price:.2f}.")
            currBudget += sold * price
        else:
            print("invalid action")
        currBudget = round(currBudget, 2)
        inputStr = input("Would you like to continue trading stocks (y/N): ")
    print()  # new line

    # One time wants
    print(f"You can spend ${currBudget:.2f} this year on things you want")
    print("Enter the items you want this year (in USD)")
    print("Think about: Trends, New pet, clothing, ...")
    oneTimeWants, oneTimeWantsPrices, oneTimeWantsValues = askWants()
    print()  # new line

    # "buy the items"
    yearlyPurchases, oneTimePurchases, happiness, amountSpent = selectBuys(
        currBudget, yearlyWantsPrices, yearlyWantsValues, oneTimeWantsValues, oneTimeWantsValues)
    yearlyLeftOver = round(currBudget - amountSpent, 2)
    print("Buy the following yearly wanted items.")
    for i in yearlyPurchases:
        print(yearlyWants[i])
    print("Buy the following one time items.")
    for i in oneTimePurchases:
        print(oneTimeWants[i])
    print(f"After buying the above items you will be {happiness} \
\"happy\" and will have ${yearlyLeftOver:.2f} left over for next year")
    print()  # new line

# Closing
print("Thank you for playing the money manager simulator!")
print("We hope you enjoyed managing your finances! ")
