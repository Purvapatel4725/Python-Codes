#Assignment-2 #Question-2


def PalindromChecker(s):
    # Reverse the string using slicing and assign it to the reversedWord variable
    reversed_Word = s[::-1]
    # Check if the reversed word is equal to the original word
    if reversed_Word == s:
        # If they are equal, the word is a palindrome, so return True
        return True
    else:
        # If they are not equal, the word is not a palindrome, so return False
        return False


# Loop indefinitely
while True:
    # Prompt the user to enter a string to check if it is a palindrome
    EnterHere = str(input("Enter the string to check if it is a palindrome: "))
    # Call the PalindromChecker function to check if the entered word is a palindrome
    output = PalindromChecker(EnterHere)
    # Check the output of the function
    if output == True:
        # If the output is True, print that the word is a palindrome
        print("The given word is a Palindrome")
    else:
        # If the output is False, print that the word is not a palindrome
        print("The given word is NOT a palindrome")

