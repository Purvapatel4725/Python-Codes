def ValidPassFunc(Value): 
    if len(Value)>=7 and any(i.isupper() for i in Value) and any(i.islower() for i in Value) and any(i.isdigit() for i in Value):
        return True
    else:
        return False


password = input("Enter a password with min len 7: ")
while ValidPassFunc(password) == False:
    password = input("Invalid password, please try again: ")
print("Valid password, Great Job")

