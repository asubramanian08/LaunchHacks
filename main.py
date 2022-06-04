from buy import selectBuys

# Introduction
print("Welcome to money manager simmulator")
# GIVE AN QUICK EXPLAINATION OF THIS GAME


def askCosts(questions):
  totalCost = 0
  
  # ask questions
  for q in questions:
    currCost = int(input(q))
    totalCost += (currCost)
  
  # additional costs
  print("Enter any additional costs (NA to quit). Write the item then the cost in dollars. These costs happen every year.")
  item = ""
  while item != "NA":
    item, currCost = input("Enter additional costs: ").split(' ')
  
    # return the total costs
  return totalCost

# get the net salery (income - taxes)
income = int(input("Enter your income per year: "))
taxes=0
if income>=625370:
  taxes+=60789.92+((income-625369)*0.123)
elif income>=375222:
  taxes+=32523.20+((income-375221)*0.113)
elif income>=312687:
  taxes+=26082.09+((income-312687)*0.103)
elif income>=61215:
  taxes+=2695.19+((income-61215)*0.093)
elif income>=48436:
  taxes+=1672.87+((income-48436)*0.08)
elif income>=34893:
  taxes+=860.29+((income-34893)*0.06)
elif income>=22108:
  taxes+=348.89+((income-22108)*0.04)
elif income>=9326 :
  taxes+=93.25+((income-9326 )*0.02)
else:
  taxes=income*0.01
# print(taxes)
income=income-taxes
# print(income-taxes)

# yearly costs
print("Please enter your yearly cost for the following items (in USD)")
yearlyCosts = askCosts(["Rent/Morgage: ", "Food: ", "Gas: ", "Electicty bill: "])
yearlyBudget = income-yearlyCosts
print(yearlyBudget)
if(yearlyBudget<0):
  print("insuficunet funds")
  exit()
else:
  print("This is how much you can spend/ have savings per year", yearlyBudget)

# yearly wants
yearlyWantsPrices = []
yearlyWantsValues = []
yearlyWants = [str]
# WRITE THIS LATER
  
# Major loop (1 iteration = 1 year)
yearsToSimmulate = int(input("How many years do you want to simmulate: "))
yearlyLeftOver = 0
for year in range(yearsToSimmulate):
  currBudget = yearlyBudget + yearlyLeftOver
  # one time costs
  currBudget -= askCosts(["Did you have any medical expensis"])
  # ASK MORE QUESTIONS
  
  # one time wants
  # WRITE THIS LATER
  oneTimeWantsPrices = []
  oneTimeWantsValues = []
  oneTimeWants = [str]
    # price + happynes

  # "buy the items"
  yearlyPurchases, oneTimePurchases, happiness, amountSpent = selectBuys(currBudget, yearlyWantsPrices, yearlyWantsValues, oneTimeWantsValues, oneTimeWantsValues)
  yearlyLeftOver = currBudget - amountSpent
  # PRINT THE ITEMS THAT WERE BOUGHT
  
  # STOCKS

# ending
print("Thank you for playing the money manager simmulator")