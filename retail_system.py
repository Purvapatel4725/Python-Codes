#Purva Patel #100886734
class RetailItem:
    def __init__(self, description, units, price):
        self.__desc = description
        self.__un = units
        self.__pr = price

    def ReturnDescription(self):
        return self.__desc

    def AssignDescription(self, description):
        self.__desc = description

    def ReturnUnits(self):
        return self.__un

    def AssignUnits(self, units):
        self.__un = units

    def ReturnPrice(self):
        return self.__pr

    def AssignPrice(self, price):
        self.__pr = price

class CashRegister:
    def __init__(self):
        self.__List = []

    def purchase_item(self, item):
        self.__List.append(item)

    def get_total(self):
        total = 0
        for i in self.__List:
            total = total + i.ReturnPrice()
        return total

    def show_items(self):
        for i in self.__List:
            print("*****************************************")
            print(f"Description: {i.ReturnDescription()}")
            print(f"Units: {i.ReturnUnits()}")
            print(f"Price: {i.ReturnPrice()}")
            print("*****************************************")

    def clear(self):
        self.__List.clear()





first = RetailItem("Jacket", 12, 59.95)
second = RetailItem("Designer Jeans", 40, 34.95)
third = RetailItem("Shirt", 20, 24.95)
a = CashRegister()
while True:
    print("*****************************************")
    print("1. Purchase Item \n2. Checkout \n3. Exit")
    print("*****************************************")
    mainMenu = int(input("Enter the number of the task you would like: "))
    if mainMenu == 1:
        print("*****************************************")
        print("1. Jacket \n2. Designer Jeans \n3. Shirt")
        print("*****************************************")
        SubMenu = int(input("Enter the item number: "))
        if SubMenu == 1:
            a.purchase_item(first)
        elif SubMenu == 2:
            a.purchase_item(second)
        elif SubMenu == 3:
            a.purchase_item(third)
        else:
            print("Please enter a valid option from the Menu")
    elif mainMenu == 2:
        a.show_items()
        print("Total:", a.get_total())
        a.clear()
    elif mainMenu == 3:
        print("Thank you for shopping with us! Have a great day ahead.")
        break
    else:
        print("Please enter a valid option from the Menu")
