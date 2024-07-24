#Purva Patel #100886734
class BasicCalculator:
    def add(self , a , b):
        return a + b

    def subtract(self , a , b):
        return a - b

    def multiply(self , a , b):
        return a * b

    def divide(self , a , b):
        if b == 0:
            raise ValueError("Input cannot be zero.")
        return a / b


class AdvancedCalculator(BasicCalculator):
    def add(self , a , b):
        try:
            result = super().add(a , b)
        except TypeError:
            raise ValueError("Invalid input! Please enter a valid input.")
        return result

    def subtract(self , a , b):
        try:
            result = super().subtract(a , b)
        except TypeError:
            raise ValueError("Invalid input! Please enter a valid input.")
        return result

    def multiply(self, a , b):
        try:
            result = super().multiply(a , b)
        except TypeError:
            raise ValueError("Invalid input! Please enter a valid input.")
        return result

    def divide(self , a , b):
        try:
            result = super().divide(a , b)
        except (TypeError, ZeroDivisionError):
            raise ValueError("Invalid input or division by zero")
        return result


def main():
    calculator = AdvancedCalculator()
    opListHistory = []

    while True:
        try:
            Input = input("What operation would you like to perform (addition,subtraction,multiplication,division): ")
            if Input.lower() in ["addition" , "add" , "+"]:
                a = float(input("Enter your first number: "))
                b = float(input("Enter your second number: "))
                answer = calculator.add(a, b)
                print(f"{a} + {b} = {answer}")
                opListHistory.append(f"{a} + {b} = {answer}")
                print("###################################################################################")

            elif Input.lower() in ["subtraction" , "-", "sub"]:
                a = float(input("Enter your first number: "))
                b = float(input("Enter your second number: "))
                answer = calculator.subtract(a, b)
                print(f"{a} - {b} = {answer}")
                opListHistory.append(f"{a} - {b} = {answer}")
                print("###################################################################################")

            elif Input.lower() in ["multiplication" , "*" , "multi"]:
                a = float(input("Enter your first number: "))
                b = float(input("Enter your second number: "))
                answer = calculator.multiply(a, b)
                print(f"{a} * {b} = {answer}")
                opListHistory.append(f"{a} * {b} = {answer}")
                print("###################################################################################")

            elif Input.lower() in ["division", "/" , "div"]:
                a = float(input("Enter your first number: "))
                b = float(input("Enter your second number: "))
                answer = calculator.divide(a, b)
                print(f"{a} / {b} = {answer}")
                opListHistory.append(f"{a} / {b} = {answer}")
                print("###################################################################################")

            elif Input.lower() == "exit" or Input.lower() == "quit":
                print("###################################################################################")
                break
            
            else:
                print("Invalid operation")
        except ValueError as e:
            print(e)

    print("Operations performed(history):")
    for op in opListHistory:
        print(op)

if __name__ == "__main__":
    main()

