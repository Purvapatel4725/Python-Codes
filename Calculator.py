# Purva Patel #100886734
a = True
print("Welcome to the calculator!")
while a == True:
    e = input("Select operations to perform (add(+), subtract(-), multiply(*), divide(/),exponential(**)) or exit/stop(exit): ").lower()
    if e == "+":
        num1 = input("Enter the first number: ") 
        if num1 == "exit":
            print("You exited the program.")
            break
        elif not num1:
            num1 == ""
            num2 = input("Enter the second number: ")
            c = float(num2) + float(c)
            print(c)
        else:
            num2 = input("Enter second number: ")
            if num2 == "exit":
                print("You exited the program.")
                break
            elif not num2:
                num2 == ""
                c = float(num1) + float(c)
                print(c)
            else:
                c = float(num1) + float(num2)
                print(c)

        b = input("would you like to continue the program (Y/N)): ").lower()
        if b == "n":
            print("You exited the program.")
            break
        c = c 



    elif e == "-":
        num1 = input("Enter the first number: ")
        if num1 == "exit":
            print("You exited the program.")
            break
        elif not num1:
            num1 == ""
            num2 = input("Enter the second number: ")
            c = float(num2) - float(c)
            print(c)
        else:
            num2 = input("Enter the second number: ")
            if num2 == "exit":
                print("You exited the program.")
                break
            elif not num2:
                num2 == ""
                c = float(num1) - float(c)
                print(c)
            else:
                c = float(num1) - float(num2)
                print(c)
        
        b = input("would you like to continue the program (Y/N)): ").lower()
        if b == "n":
            print("You exited the program.")
            break 
        c = c
        


    elif e == "/":
        num1 = input("Enter the first number: ")
        if num1 == "exit":
            print("You exited the program.")
            break
        elif not num1:
            num1 == ""
            num2 = input("Enter the second number: ")
            c = float(num2) / float(c)
            print(c)
        else:
            num2 = input("Enter the second number: ")
            if num2 == "exit":
                print("You exited the program.")
                break
            elif not num2:
                num2 == ""
                c = float(num1) / float(c)
                print(c)
            else:
                c = float(num1) / float(num2)
                print(c)

        b = input("Do you want to continue(Y/N)): ").lower()
        if b == "n":
            print("You exited the program.")
            break
        c = c
    


    elif e == "*":
        num1 = input("Enter the first number: ")
        if num1 == "exit":
            print("You exited the program.")
            break
        elif not num1:
            num1 == ""
            num2 = input("Enter the second number: ")
            c = float(num2) * float(c)
            print(c)
        else:
            num2 = input("Enter the second number: ")
            if num2 == "exit":
                print("You exited the program.")
                break
            elif not num2:
                num2 == ""
                c = float(num1) * float(c)
                print(c)
            else:
                c = float(num1) * float(num2) 
                print(c)

        b = input("would you like to continue the program (Y/N)): ").lower()
        if b == "n":
            print("You exited the program.")
            break
        c = c 
    


    elif e == "**": 
        num1 = input("Enter base: ")
        if num1 == "exit":
            print("You exited the program.")
            break
        elif not num1:
            num1 == ""
            num2 = input("Enter power: ")
            d = 1
            for i in range(int(num2)):
                d = d*int(c)
            print(d)
        else:
            num2 = input("Enter power: ")
            if num2 == "exit":
                print("You exited the program.")
                break
            elif not num2:
                num2 == ""
                d = 1 
                for i in range(int(c)):
                    d = d*int(c)
                print(d)
            else:
                d = 1
                for i in range(int(num2)):
                    d = d*int(num1)
                print(d)

        b = input("would you like to continue the program (Y/N)): ").lower()
        if b == "n":
            print("You exited the program.")
            break
        c = d



    elif e == "exit":
        print("You exited the program.")
        break
    





    



    

