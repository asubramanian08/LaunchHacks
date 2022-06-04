#from buy import selectBuys


income = int(input("Enter your income per year: "))
yearlyBudget = income
def askCosts(questions):
  totalCost = 0
  
  # ask questions
  for q in questions:
    currCost = int(input(q))
    totalCost += (currCost)
  
  # additional costs
  print("Enter any additional costs (NA to quit). Write the item then the cost in dollars. Per year")
  item = ""
 
  while item != "NA":
   
   # item, currCost = input("Enter additional costs: ").split(' ')
    
    item=input("Enter additional costs: ")
    if item !="NA":
      totalCost+=int(item)
  # return the total costs
  return income-totalCost  
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
print(taxes)
income=income-taxes
print(income-taxes)
# yearly costs
print("Please enter your yearly cost for the following items (in USD)")
yearlyCosts = askCosts(["Rent/Morgage: ", "Food: ", "Gas: ", "Electicty bill: "])
new_yearlyCosts=yearlyCosts
print(new_yearlyCosts)
  # rent = int(input(questions))
  # longterm_goal = int(input(questions))
  # food = int(input(questions))
  # gas_electricty_bill = int(input(questions))
  # gas = int(input(questions)
#yearly costs

# number
#print(yearlyCosts)
#of elements as input










#for q in questions:
 # cost = int(input(q))
  #yearlyBudget = yearlyBudget - cost
#for i in range(4):
 # print(questions)

# yearly wants
#itemPrices = [] # 

#n = int(input("type in the umber of the amount of items : "))
  
# iterating till the range
#for i in range(0, n):
   # ele = int(input())
  
 #   itemPrices.append(ele) # adding the element
      
#print(lst)

#itemValues = [] # happiness value



# MAJOR LOOP
#for m in nextyear:
  
  # ask for one time costs
  # ask for one time wants
    # price + happynes
  # STOCKS

#rent = int(input("Enter your rent: "))
#longterm_goal = int(input("Enter the amount of money for your longterm #unneededgoal: "))
#food = int(input("Enter your daily food cost: "))
#gas_electricty_bill = int(input("Enter your yearly electricity/gas bill: "))
#gas = int(input("How many times a year do you fll up gas: "))time=retirment-age
#x=1000000/time
#y=x/12
#spending=income-rent-longterm_goal-30*food-gas_electricty_bill-gas*7-y
#spendings=0.0725*spending
#h=spendings-900
#print(h)
#if(h<0):
  #print("hi")
