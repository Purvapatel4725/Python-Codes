#Purva Patel #100886734
import random
import time
correct = 0
count = 0
totalquestions = 5
startTime = time.time()
while totalquestions > count:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9) 
    question = num1 ** num2
    answer = int(input(f"{count + 1}.) What is {num1} ** {num2}: "))
    if answer == question:
        print("You are correct!")
        correct = correct + 1
    else:
        print("Your are wrong!")
        print(f"The correct answer is: {num1 ** num2}")
    endtime = time.time()    
    count = count + 1
    if count == 5:
        print(f"The number of points recived are {correct} out of 5 Total time take is {int(endtime) - int(startTime)}")
        retake = input("Do you want to retake the quiz? Type Y/N: ").lower()
        if retake == "n":
            print("You choose to exit the quiz!")
            break
        else:
            correct = 0
            count = 0
            totalquestions = 5
            startTime = time.time()
            continue



