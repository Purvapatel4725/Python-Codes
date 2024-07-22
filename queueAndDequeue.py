class Queue:
    def __init__(self):
        self.list = []

    def addToQueue(self, item):
        self.list.append(item)

    def removeFromQueue(self):
        if self.list:
            return self.list.pop(0)
        else:
            return None

    def size(self):
        return len(self.list)
    

class1 = Queue()
class1.addToQueue(27)
class1.addToQueue(50)
class1.addToQueue(40)
print(f"Size of queue: {class1.size()}")
print(f"Removed item item: {class1.removeFromQueue()}")
print(f"Size of queue: {class1.size()}")