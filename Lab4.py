#Purva Patel #100886734
import random
class Vehicle:
    def __init__(self, manufacturer, model, wheels, typeOfVehicle, seats):
        self.manufacturer = manufacturer
        self.model = model
        self.wheels = wheels
        self.typeOfVehicle = typeOfVehicle
        self.seats = seats

    def printDetails(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Wheels: {self.wheels}")
        print(f"Type of Vehicle: {self.typeOfVehicle}")
        print(f"Seats: {self.seats}")

    def checkInfo(self, **kwargs):
        for key, value in kwargs.items():
            if getattr(self, key) == value:
                print(f"{key} : True")
            else:
                print(f"{key} : False")


class Car(Vehicle):
    def __init__(self, manufacturer, model, wheels, typeOfVehicle, seats, manufacturingNumber):
        super().__init__(manufacturer, model, wheels, typeOfVehicle, seats)
        self.manufacturingNumber = manufacturingNumber
        print("A car was created!")

    def printDetails(self):
        super().printDetails()
        print(f"Manufacturing Number: {self.manufacturingNumber}")


class Truck(Vehicle):
    def __init__(self, manufacturer, model, wheels, typeOfVehicle, seats, manufacturingNumber):
        super().__init__(manufacturer, model, wheels, typeOfVehicle, seats)
        self.manufacturingNumber = manufacturingNumber
        print("A truck was created!")

    def printDetails(self):
        super().printDetails()
        print(f"Manufacturing Number: {self.manufacturingNumber}")


class Motorcycle(Vehicle):
    def __init__(self, manufacturer, model, wheels, typeOfVehicle, seats, manufacturingNumber):
        super().__init__(manufacturer, model, wheels, typeOfVehicle, seats)
        self.manufacturingNumber = manufacturingNumber
        print("A motorcycle was created!")

    def printDetails(self):
        super().printDetails()
        print(f"Manufacturing Number: {self.manufacturingNumber}")


def createVehicles(manufacturers, models, seats, total):
    vehicles = []
    for i in range(5):
        typeOfVehicle = random.choice(list(models.keys()))
        manufacturingNumber = total[typeOfVehicle] + 1
        total[typeOfVehicle] += 1
        vehicle = eval(typeOfVehicle)(
            random.choice(manufacturers),
            random.choice(models[typeOfVehicle]),
            random.randint(2, 4),
            typeOfVehicle,
            random.choice(seats[typeOfVehicle]),
            manufacturingNumber)
        vehicles.append(vehicle)
    return vehicles



def main():
    manufacturers = ["Toyota", "GM", "Ford", "Jeep", "Audi"]
    models = {'Car': ["X11", "i3", "XFCE"], "Truck": ["Linux", "Unix", "FreeBSD"], "Motorcycle": ["Triforce", "Mushroom", "Morphball"]}
    seats = {"Car": [2, 3, 4, 5], "Truck": [2, 3, 4], "Motorcycle": [1, 2]}
    total = {"Car": 0, "Truck": 0, "Motorcycle": 0}
    vehicles = createVehicles(manufacturers, models, seats, total)
    vehicle = random.choice(vehicles)
    print("\t")
    vehicle.printDetails()
    print("\t")
    vehicle.checkInfo(model= False)
    print("\t")
    print(f"Car: {total['Car']}, Truck: {total['Truck']}, Motorcycle: {total['Motorcycle']}")

if __name__ == "__main__":
    main()