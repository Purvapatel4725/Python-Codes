#Purva Patel #100886734
import string
def getStringInfo(*args):
    convertList = [*args]
    for a in convertList:
        countWords1 = a.split(" ")
        lengthOfString = len(a)
        countWordsExS = a.replace(" ","")
        newList1 = len([c for c  in a if c.isalpha()])
        newList2 = len([c for c in a if c.isdigit()])
        digitCheck = a.isdigit()
        newList3 = len([c for c in a if c in string.punctuation])
        newList4 = len([c for c in a if c.isupper()])
        newList5 = len([c for c in a if c.islower()])
        Uppercase = a.upper()
        Lowercase = a.lower()
        Reversecase = a.swapcase()
        title = a.title()




        print(f"# of words              - {len(countWords1)}")
        print(f"# of  Chars             - {lengthOfString}")
        print(f"# of char (Excl. w/s)   - {len(countWordsExS)}")
        print(f"# of letters            - {newList1}")
        print(f"# of numbers            - {newList2}")
        print(f"# of punctuation        - {newList3}")
        print(f"Is number               - {digitCheck}")
        print(f"# of Uppercase Chars    - {newList4}")
        print(f"# of Lowercase Chars    - {newList5}")
        print(f"Uppercase               - {Uppercase}")
        print(f"Lowercase               - {Lowercase}")
        print(f"Reversecase             - {Reversecase}")
        print(f"No Space                - {countWordsExS}")
        print(f"Title                   - {title}")
        print(f"Reversed                - {a[::-1]}")
        print("##############################################################################################################")

getStringInfo("HeLlO wOrLd!!11","Did you hear about the one-eyed one-horned Flying Purple People Eater?")