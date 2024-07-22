#Purva Patel  #100886734 
import random
import time
count = 0
print("The quiz has started!")
totalquestions = 0
correct = [] 
storedtime = []
while count == 0:
   c = 0
   startTime = time.time()
   if c == 0:
      num1 = random.randint(0,9)
      num2 = random.randint(0,9)
      question = num1**num2
      answer = int(input(f"what is {num1}**{num2}: "))
      if answer == question:  
         i = True
      else:
         i = False 

   if i == True:
      print("You are correct!")
      correct.append(1)
   else:
      print("Your are wrong!")
      print(f"Correct answer is: {question}")
      correct.append(0)
   endTime = time.time()
   timeDiffrence = int(endTime)-int(startTime)
   storedtime.append(timeDiffrence)
   totalquestions = totalquestions + 1
   if totalquestions == 5:
      score = int(correct[0]) + int(correct[1])+ int(correct[2])+ int(correct[3])+ int(correct[4])
      totaltime = int(storedtime[0])+ int(storedtime[1])+ int(storedtime[2])+ int(storedtime[3])+ int(storedtime[4])
      print(f"The number of points received {score} are out of 5 Total Time taken is {totaltime} seconds")
      retake = input("Do you want to retake the quiz? Type Y/N: ").lower()
      if retake == "n":
         print("You choose not to retake the quiz. quiz ended")
         break
      elif retake == "y":
         correct.pop(0)
         correct.pop(0)
         correct.pop(0)
         correct.pop(0)
         correct.pop(0)
         storedtime.pop(0)
         storedtime.pop(0)
         storedtime.pop(0)
         storedtime.pop(0)
         storedtime.pop(0)
         totalquestions = 0
         continue
        

         


