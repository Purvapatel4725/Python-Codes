#Assignment-2 #Question-1

def ReverseText(s):  # Function definition to reverse a string
    if len(s) <= 1:  # Check if the length of the string is 1 or less than 1
        return s  # Return the string as it is
    else:
        return ReverseText(s[1:]) + s[0]  # Recursively call the function on the all characters except the first one and append the first character at the end



a = 0  #Counter (used for to keep the number of times the loop will run to take the input from the user)
while True:   #Starts loop
    EnterHere = str(input(f"{a+1}).Enter a string that you want to reverse: "))   #Takes input from the user
    Output = ReverseText(EnterHere) #Function called
    print(Output)  #Printing the output
