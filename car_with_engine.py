#Purva Patel #100886734
#question 5
class Engine:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume
    
    def __str__(self):
        return f"The engine has {self.power} horsepower and {self.volume} liters Volume"


class Car:
    def __init__(self, name, color, engine):
        self.name = name
        self.color = color
        self.engine = engine
    
    def __str__(self):
        return f"This is a {self.color} {self.name}"
    
    
def main():
    MyEngine = Engine(200, 2000)
    MyCar = Car("Audi", "white", MyEngine)
    print(MyEngine)
    print(MyCar)
    
    
if __name__ == "__main__":
    main()
