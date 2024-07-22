# Purva Patel #100886734 # Question 5
def bal():
    iv = int(input("enter the initial value: "))
    r = int(input("enter the rate of intrest: "))
    y = int(input("enter the number of years: "))
    step1 = r/100
    step2 = 1 + step1
    step3 = step2**y
    step4 = step3*iv
    return step4

print(bal())