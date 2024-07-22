#Purva Patel #100886734

class Lab1:
    def __init__(self, first = 0, second = 0, third = 0):
        self.first = first
        self.second = second
        self.third = third
        self.numList = [first, second, third]
        for i in self.numList:
            if not isinstance(i,int):
                print("Numbers are not in Integer format")
                return 0

    def firstGreaterThanSecond(self):
        return self.compareNum(self.first, self.second)

    def firstGreaterThanThird(self):
        return self.compareNum(self.first, self.third)

    def secondGreaterThanFirst(self):
        return self.compareNum(self.second, self.first)

    def secondGreaterThanThird(self):
        return self.compareNum(self.second, self.third)

    def thirdGreaterThanFirst(self):
        return self.compareNum(self.third, self.first)
    
    def thirdGreaterThanSecond(self):
        return self.compareNum(self.third, self.second)

    def compareNum(self, num1, num2):
        if num1 > num2:
            return True
        else:
            return False

    def largestNum(self):
        return max(self.numList)

    def SmallestNum(self):
        return min(self.numList)

    def Allequal(self):
        if self.first == self.second == self.third:
            return True
        else:
            return False

    

    
try: 
    a = int(input("Enter the First number to compare: ")) 
except:
    a = 0 

try:
    b = int(input("Enter the second number to compare: "))
except:
    b = 0

try:
    c = int(input("Enter the third number to compare: "))
except:
    c = 0
CheckNumbers = Lab1(a,b,c)
print(CheckNumbers.firstGreaterThanSecond())
print(CheckNumbers.firstGreaterThanThird())
print(CheckNumbers.secondGreaterThanFirst())
print(CheckNumbers.secondGreaterThanThird())
print(CheckNumbers.thirdGreaterThanFirst())
print(CheckNumbers.thirdGreaterThanSecond())
print(CheckNumbers.largestNum())
print(CheckNumbers.SmallestNum())
print(CheckNumbers.Allequal())



    
    

