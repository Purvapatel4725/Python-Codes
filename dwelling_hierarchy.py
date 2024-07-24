#Purva Patel #100886734
class Dwelling:
    def __init__(self, typeOfDwelling, value, rooms):
        self.typeOfDwelling = typeOfDwelling
        self.value = value
        self.rooms = rooms
    
    def printData(self):
        print(f"Dwelling Type:{self.typeOfDwelling}")
        print(f"Value:{str(self.value)}")
        print(f"Rooms:{str(self.rooms)}")
    
    def get_dwellingType(self):
        return self.typeOfDwelling
    
    def __str__(self):
        return f"Dwelling Type:{self.typeOfDwelling} \nValue:{str(self.value)} \nRooms:{str(self.rooms)}"

class House(Dwelling):
    def __init__(self, typeOfDwelling, value, rooms, address, numOfFloors):
        super().__init__(typeOfDwelling, value, rooms)
        self.address = address
        self.numOfFloors = numOfFloors
    
    def printData(self):
        super().printData()
        print(f"Address:{self.address}")
        print(f"NumberOfFloors:{str(self.numOfFloors)}")
    
    def __str__(self):
        return super().__str__() + f"\nAddress:{self.address} \nNumberOfFloors:{str(self.numOfFloors)}"


class Apartment(Dwelling):
    def __init__(self, typeOfDwelling, value, rooms, address, apartmentNumber):
        super().__init__(typeOfDwelling, value, rooms)
        self.address = address
        self.apartmentNumber = apartmentNumber
    
    def printData(self):
        super().printData()
        print(f"Address:{self.address}")
        print(f"ApartmentNumber:{str(self.apartmentNumber)}")
    
    def __str__(self):
        return super().__str__() + f"\nAddress:{self.address} \nApartmentNumber:{str(self.apartmentNumber)}"


if __name__ == "__main__":
    house = House("House", 800, 100, "1911 Simcoe St", 4)
    apartment = Apartment("Apartment", 500, 1, "100 York St", 3087)
    print(house.get_dwellingType())
    house.printData()
    print("\t")
    print(house)
    print("\t")
    print(apartment.get_dwellingType())
    apartment.printData()
    print("\t") 
    print(apartment)
