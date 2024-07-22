#Purva Patel # 100886734 # Question 7
import random
comp = random.randint(0,100)
b = True
print("Computer has guessed the number....It's your turn!")
while b == True:
    a = int(input("Guess the number: "))
    if a > comp:
        print("The guess is too high, try again!")
    elif a < comp:
        print("It is too low, try again!")
    elif a == comp:
        print("Congrats! your guess is correct.")
        comp = random.randint(0,100)
        continue