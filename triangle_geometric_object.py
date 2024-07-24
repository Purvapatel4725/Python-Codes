#Purva Patel #100886734
#question 3
class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled
    
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def isFilled(self):
        return self.__filled
    
    def setFilled(self, filled):
        self.__filled = filled
    
    def __str__(self):
        return "color: " + self.__color + " and filled: " + str(self.__filled)

class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0, color = "green", filled = True):
        super().__init__(color, filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getSide3(self):
        return self.__side3
    
    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = (s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)) ** 0.5
        return area
    
    def getPerimeter(self):
        perimeter = self.__side1 + self.__side2 + self.__side3
        return perimeter
    
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)


def main():
    side1 = float(input("Enter the side 1: "))
    side2 = float(input("Enter the side 2: "))
    side3 = float(input("Enter the side 3: "))
    color = input("Enter a color: ")
    filledUnfilled = bool(int(input("Enter (1) for filled or (0) for not filled: ")))

    triangle = Triangle(side1, side2, side3, color, filledUnfilled)

    print(f"Area: {triangle.getArea()}")
    print(f"Perimeter: {triangle.getPerimeter()}")
    print(f"Color: {triangle.getColor()}")
    print(f"Filled: {triangle.isFilled()}")
    print(triangle)

if __name__ == "__main__":
    main()
