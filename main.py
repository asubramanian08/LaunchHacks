import random
 
totalScore = []

 
class user:
   def __init__(self):
       self.testScore = 0
      
       self.location = input("Which continent do you live on? ")
       self.name = input(
           "What is your first and last name (suggested format: First + space + Last)\nexample: Michael Jordan "
       )
 
   def getScore(self):
       print("COVID-19 Test score is: " + str(self.testScore) + " points.\n"+"out of 10")
    
 
   def getLocation(self):
       print(self.location)
 
   def getName(self):
       print(self.name)
 
   def updateTestScore(self):
       self.testScore = self.testScore + 1
 
   def updateFScore(self):
       self.testScore = self.testScore + 1
 
 
class questionBank:
   def __init__(self):
   
       self.testQuestionArray = []
  
 
       self.totalQuestions = 6
       self.questions()
   def questions(self):
       self.testQuestionArray.append(
           "What is your income"
       )
       self.testQuestionArray.append(
           "One long term goal and the cost"
       )
       self.testQuestionArray.append(
           "What is your age"
       )
       self.testQuestionArray.append(
           "When do you want to retire"
       )
          
       self.testQuestionArray.append(
           "How much do you spend on food")
     
       self.testQuestionArray.append(
           "What was your last gas/electricy bill")





 # this file will just take the input given by @Chandu, call the functions, and send back the output to @Chandu