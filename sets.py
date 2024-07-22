#Purva Patel #100886734
def checkvowelsConsonants():
    global listSentence
    countVowels = 0
    countConsonants = 0
    countSpecial = 0
    countNumbers = 0
    setVowel = {"A","E","I","O","U","a","e","i","o","u"}
    setSpecial = {"!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]",":",";","\"","\'","<",">",",",".","?","/","~","`","\\","|","“","”"," "}
    setNumbers = {"1","2","3","4","5","6","7","8","9","0"}
    for i in listSentence:
        if i in setVowel:
            countVowels += 1
        elif i in setSpecial:
            countSpecial += 1
        elif i in setNumbers:
            countNumbers += 1
        else:
            countConsonants += 1
    print(f"The number of vowels is {countVowels} and consonants is {countConsonants}")

        


while True:
    print("________________________________________________________________________________")
    print("Options are as below:")
    print("---->\t1. Print the number of vowels and consonants")
    print("---->\t2. Exit the program")
    enterInput = input("What would you like to do(1 or 2)? ")
    if enterInput == "2":
        print("You exited the program.")
        break
    elif enterInput == "1":
        sentence = input("Enter any sentence: ")
        listSentence = list(sentence)
        checkvowelsConsonants()
