#Purva Patel #100886734
balance = float(0)
otherBalance = float(0)

def getBalance():
    return balance

def getOtherbalance():
    return otherBalance

def printBalances():
    global balance
    global otherBalance
    print(f"\tbalance: ${balance}")
    print(f"\totherBalance: ${otherBalance}")

def deposit(money):
    global balance
    if money < 0:
        print("invalid input! Money enter should be greater than zero")
    else:
        balance = balance + money
        print("Money deposit successful!")

def withdraw(money):
    global balance
    if money < 0:
        print("Invalid input! Money entered should be greater than Zero and less than or equal to balance")
    elif money > balance:
        print("Invalid input! Money entered should be greater than Zero and less than or equal to balance")
    else:
        balance = balance - money
        print("Money has been withdrawn successfully!")

def transfer(money):
    global balance
    global otherBalance
    if money < 0:
        print("Invalid input! Money entered should be greater than Zero and less than or equal to balance")
    elif money > balance:
        print("Invalid input! Money entered should be greater than Zero and less than or equal to balance")
    else:
        balance = balance - money
        otherBalance = money + otherBalance
        print("Money has been transfered from balance to other balance")



enterLoop = True
while enterLoop == True:
    print("________________________________________________________________________________")
    print("Options are as below:")
    print("---->\t1. Get Balance")
    print("---->\t2. Get Other Balance")
    print("---->\t3. Print both Balances")
    print("---->\t4. Deposit")
    print("---->\t5. Withdraw")
    print("---->\t6. Transfer")
    print("---->\t7. Exit/Stop")
    enter = str(input("Enter an option: "))
    if enter == "1":
        a = getBalance()
        print(a)
    elif enter == "2":
        b = getOtherbalance()
        print(b)
    elif enter == "3":
        c = printBalances()
    elif enter == "4":
        money = float(input("\tEnter any amount to deposite: $"))
        d = deposit(money)
    elif enter == "5":
        money = float(input("\tEnter any amount to withdraw: $"))
        e = withdraw(money)
    elif enter == "6":
        money = float(input("\tEnter any amount to transfer: $"))
        f = transfer(money)
    elif enter == "7":
        print("You exited the ATM machine!")
        break







    


    
