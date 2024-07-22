class Point:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    
    def show(self):
        print(f"({self.x1},{self.x2})")

    def move(self,a,b):
        self.x1 = self.x1 + a
        self.x2 = self.x2 + b
    
    def dist(self,x0):
        return ((self.x1 - x0.x1)**2 + (self.x2 - x0.x2)**2)**0.5


p1 = Point(2,3)
p2 = Point(3,3)
p1.show()
p2.show()
p1.move(10,-10)
p1.show()
p2.show()
print(p1.dist(p2))