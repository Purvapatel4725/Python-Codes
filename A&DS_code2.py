#Assginment-1 #Question-2

from abc import ABC, abstractmethod

# Abstract base class for polygons
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Triangle class inheriting from Polygon
class Triangle(Polygon):
    def __init__(self, side1, side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        # Using heron's formula over here
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Quadrilateral class inheriting from Polygon
class Quadrilateral(Polygon):
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def area(self):
        # Assuming it's a rectangle
        return self.side1 * self.side2

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

# Pentagon class inheriting from Polygon
class Pentagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 1.72048 * self.side ** 2

    def perimeter(self):
        return 5 * self.side

# Hexagon class inheriting from Polygon
class Hexagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 2.5981 * self.side ** 2

    def perimeter(self):
        return 6 * self.side

# Octagon class inheriting from Polygon
class Octagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 2 * (1 + 2 ** 0.5) * self.side ** 2

    def perimeter(self):
        return 8 * self.side

# IsoscelesTriangle class inheriting from Triangle
class IsoscelesTriangle(Triangle):
    def __init__(self, base, height, side):
        super().__init__(base, height)
        self.side = side

    def perimeter(self):
        return 2 * self.side + self.base

# EquilateralTriangle class inheriting from Triangle
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, (3 ** 0.5) / 2 * side)

    def perimeter(self):
        return 3 * self.base

# Rectangle class inheriting from Quadrilateral
class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)

    def area(self):
        return self.side1 * self.side2

# Square class inheriting from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)



MyList = []
NumPolygons = 0
# Get the number of polygons from the user
while True:
    try:
        NumPolygons = int(input("Enter the number of polygons: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Create polygons based on user input
for i in range(NumPolygons):
    print(f"\nPolygon {i+1}:")
    
    while True:
        PolygonType = input("Select the Type of polygon:\nfor example:\nTriangle\nQuadrilateral\nPentagon\nHexagon\nOctagon: ")
        try:
            if PolygonType == "Triangle":
                side1 = float(input("Enter the length of side 1: "))
                side2 = float(input("Enter the length of side 2: "))
                side3 = float(input("Enter the length of side 3: "))
                Pol = Triangle(side1, side2, side3)

            elif PolygonType == "Quadrilateral":
                side1 = float(input("Enter the length of side 1: "))
                side2 = float(input("Enter the length of side 2: "))
                side3 = float(input("Enter the length of side 3: "))
                side4 = float(input("Enter the length of side 4: "))
                Pol = Quadrilateral(side1, side2, side3, side4)

            elif PolygonType == "Pentagon":
                side = float(input("Enter the length of side: "))
                Pol = Pentagon(side)

            elif PolygonType == "Hexagon":
                side = float(input("Enter the length of side: "))
                Pol = Hexagon(side)

            elif PolygonType == "Octagon":
                side = float(input("Enter the length of side: "))
                Pol = Octagon(side)
                
            else:
                print("Invalid polygon type. Try Again!")
                continue

            MyList.append(Pol)
            break

        except ValueError:
            print("Invalid input. Please try again with a valid input.")


print("\nPolygon Details:")
for i, Pol in enumerate(MyList):  #gives the final output of the details 
    print(f"\nPolygon {i+1}:")
    print("Area:", Pol.area())
    print("Perimeter:", Pol.perimeter())
