#Purva Patel #100886734 # Question 2
def fin():
    a = int(input("Enter the family income: "))
    b = int(input("The number of children in family: "))
    if 30000 <= a <= 40000:
        if b >= 3:
            return b*1000
    elif 20000 <= a <= 30000:
        if b >= 2:
            return b*1500
    elif a > 20000:
        if b >= 0:
            return b*1000


print(fin())
            



