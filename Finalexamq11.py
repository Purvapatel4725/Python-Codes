#Purva Patel #100886734
#question 11
from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self):
        self.width = 0
        self.height = 0
    
    def input_sides(self):
        self.width = float(input("Enter width: "))
        self.height = float(input("Enter height: "))
    
    @abstractmethod
    def area(self):
        pass

class Triangle(Polygon):
    def __init__(self):
        super().__init__()
        self.input_sides()
    
    def area(self):
        return 0.5 * self.width * self.height



def main():
    triangle = Triangle()
    print("Area of triangle:", triangle.area())

if __name__ == "__main__":
    main()

