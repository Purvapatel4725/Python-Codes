class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a_ = a
        self.__b_ = b
        self.__c_ = c
        
    def geta(self):
        return self.__a_
    
    def getb(self):
        return self.__b_
    
    def getc(self):
        return self.__c_
    
    def getDiscriminant(self):
        return self.__b_**2 - 4*self.__a_*self.__c_
    
    def getRoot1(self):
        discriminant = self.getDiscriminant()
        if discriminant<0:
            return 0
        else:
            upper = -self.__b_ + discriminant**0.5
            lower = 2*self.__a_
            value = upper/lower
            return value

    def getRoot2(self):
        discriminant = self.getDiscriminant()
        if discriminant < 0:
            return 0
        elif discriminant == 0:
            return -self.__b_/(2 * self.__a_)
        else:
            sqrt_discriminant = discriminant ** 0.5
        if self.__b_ < 0:
            return (-self.__b_ - sqrt_discriminant)/(2 * self.__a_)
        else:
            return (-self.__b_ + sqrt_discriminant)/(2 * self.__a_)




def main():
    while True:
        try:
            inputValues = input("Enter values of a, b, c (Seprated by commas): ")
            a, b, c = map(float, inputValues.split(','))
            equation = QuadraticEquation(a,b,c)
            discriminant = equation.getDiscriminant()
            if discriminant > 0:
                root1 = equation.getRoot1()
                root2 = equation.getRoot2()
                print(f"The equation has two roots as follows: {root1} and {root2}")
            elif discriminant == 0:
                root = equation.getRoot1()
                print(f"The equation has one root as follows: {root}")
            else:
                print("The equation has no roots.")
        except:
            print("Invalid input. Please enter valid values for a, b, and c separated by commas.")



if __name__ == '__main__':
    main()
