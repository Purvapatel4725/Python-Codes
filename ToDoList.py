#Purva Patel #100886734
from datetime import datetime
def addNewItems():
    global ToDoList
    taskName = input("Enter the name of the task: ")
    if checkItemExists(taskName):
        print("Task already exist! Select the options again.")
    else:
        TaskDate = input("Enter the Date and time in yyyy/mm/dd HH:MM:SS format: ")
        CurrentDate = datetime.now()
        StrpTime1 = datetime.strptime(TaskDate , "%Y/%m/%d %H:%M:%S")
        if CurrentDate > StrpTime1:
            print("Time entered is in the past! Select the options again")
        else:
            x = (StrpTime1 , taskName)
            ToDoList.append(x)
            print("Task added successfully!")
            ToDoList.sort(reverse= False, key= takeSecond)


def checkItemExists(taskName):
    global ToDoList
    tempList = []
    for i in ToDoList:
        tempList.append(i[1])
    for i in tempList:
        if i == taskName:
            return True


def takeSecond(element):
    return element[1]


def printListItems():
    global ToDoList
    for i,element in enumerate(ToDoList, 0):
        print(f"{i}. {element[0]} - {element[1]}")


def removeListItems():
    global ToDoList
    DelTuple = int(input("Enter the index of the task you would like to delete: "))
    del ToDoList[DelTuple]
    print("The task was successfuly removed.")






ToDoList = []
while True:
    print("________________________________________________________________________________")
    print("Options are as below:")
    print("---->\t1. Enter a new To Do item")
    print("---->\t2. Print the list of all To Do items")
    print("---->\t3. Remove a To do items")
    print("---->\t4. exit the program")
    enter = str(input("What would you like to do(1,2,3 or 4)? "))
    if enter == "4":
        print("you exited the program.")
        break
    elif enter == "1":
        taskName = addNewItems()
    elif enter == "2":
        printListItems()
    elif enter == "3":
        removeListItems()
        