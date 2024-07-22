#Purva Patel #100886734
def CheckEvenOdd(mylist):
    odd = []
    even = []
    for i in mylist:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 != 0:
            odd.append(i)
    return odd , even                               
            
def CalculateAverage(mylist):
    odd , even = CheckEvenOdd(mylist)
    o = 0
    e = 0
    for i in odd:
        o = o + i    
    for i in even:
        e = e + i

    averageOdd = o // len(odd)
    averageEven = e // len(even)
    return averageEven , averageOdd
    
    
def PrintResults(avgeven, avgodd):
    print(avgeven)   
    print(avgodd) 


def CalculatePow(mylist):
    empty = []
    for i in range(len(mylist)):
        pow1 = pow(mylist[i], i)
        empty.append(pow1)
    return empty
    


Condition = True
while True:
    mylist = []
    while Condition == True:
        inputNumber = input("Enter number: ")
        if inputNumber == "-1":
            break
        else:
            mylist.append(int(inputNumber))
    print(CheckEvenOdd(mylist))
    odd , even = CalculateAverage(mylist) 
    PrintResults(even , odd)
    print(CalculatePow(mylist))
    inputCon = input("Would you like to continue(Y/N): ").lower()
    if inputCon == "n":
            print("You exited the program.")
            break
   
    











