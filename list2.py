def FindSum(mylist):
    resultlist = []
    sum = 0
    for n in mylist:
        sum = n*(n+1)//2
        resultlist.append(sum)
    return resultlist


def PrintResults(mylist,resultlist):
    for i in range(len(mylist)):
        print("Sum of " + str(mylist[i]) + " is: " + str(resultlist[i]))


def SaveResult(mylist,resultlist):
    fileOpen = open("result.txt","w")
    stringSave = ""
    for i in range(len(mylist)):
       stringSave = "Sum of " + str(mylist[i]) + " is: " + str(resultlist[i]) + "\n" 
       fileOpen.write(stringSave)
    fileOpen.close()
    print("Saved to the file...")


while True:
    mylist = []
    while True:
        try: 
            inputNumber = int(input("Enter number: "))
            if inputNumber == -1:
                break
            elif inputNumber < 0:
                print("enter positive number")
            else:
                mylist.append(inputNumber)
        except:
            print("Invalid input")
    resultlist = FindSum(mylist)
    PrintResults(mylist,resultlist) 
    SaveResult(mylist,resultlist)
    inputCon = input("Would you like to continue(Y/N): ").lower()
    if inputCon == "n":
        print("You exited the program.")
        break
