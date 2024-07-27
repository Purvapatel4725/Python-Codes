#Purva Patel #100886734
class Information:
    def __init__(self, name, age, address = "unknown", phn = "N/A"):
        self.__n = name
        self.__a = age
        self.__ad = address
        self.__phn = phn

    def name(self):
        return self.__n

    def AssignName(self, name):
        self.__n = name

    def age(self):
        return self.__a

    def AssignAge(self, age):
        self.__a = age

    def address(self):
        return self.__ad

    def AssignAddress(self, address):
        self.__ad = address

    def phonenumber(self):
        return self.__phn

    def AssignPhn(self, phn):
        self.__phn = phn

    def __str__(self):
        return f"name: {self.__n} - age: {self.__a} - address: {self.__ad}"


def display_info(person):
    print(f" Name: {person.name()}")
    print(f" Age: {person.age()}")
    print(f" Address: {person.address()}")
    print(f" Phone: {person.phonenumber()}") 

if __name__ == "__main__":
    h1 = Information("Sarah Jones", 21, "2000 Simcoe North","+1 9123405999")
    print(h1)
    display_info(h1)
    

    
