# you shouldn't be printing or asking for input in this function. That is reserved for the main.py


income = int(input("Enter your income per month: "))
rent = int(input("Enter your rent: "))
longterm_goal = int(input("Enter the amount of money for your longterm unneededgoal: "))
food = int(input("Enter your daily food cost: "))
gas_electricty_bill = int(input("Enter your monthly electricity/gas bill: "))
gas = int(input("How many times a month do you fll up gas: "))
age=int((input("How old are you?")))
retirment=int((input("When do you plan retiring")))
time=retirment-age
x=1000000/time
y=x/12
spending=income-rent-longterm_goal-30*food-gas_electricty_bill-gas*7-y
spendings=0.0725*spending
h=spendings-900
print(h)
if(h<0):
  print("hi")