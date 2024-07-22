import random 

def FunctionToGenerateRandomNumber(filename, NoofNumbers):
    fileOpen = open(filename, "w")
    for i in range(NoofNumbers):
        randomNumberGenerate = random.randint(1, 500)
        fileOpen.write(f"{randomNumberGenerate}\n")
    fileOpen.close()

NameOfFile = input("Enter the name of the file to which results should be written: ")
NumberOfRandomInt = int(input("Enter the number of random numbers to be written to the file: "))

FunctionToGenerateRandomNumber(NameOfFile, NumberOfRandomInt)