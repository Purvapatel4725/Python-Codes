#Assignment-1 #Question-1
counter = 0  # Initialize a counter variable
list_store = []  # Create an empty list to store the numbers

while counter < 10:  # Loop until counter reaches 10
    unique_number = input("Enter any number: ")  # Prompt the user for input

    if unique_number == "q" or unique_number == "Q":  # Check if user wants to quit
        break

    try:  # Try to convert the input to an integer
        num = int(unique_number)
    except:  # Handle the exception if input is not a valid integer
        print("Invalid output.")
        continue

    if num in list_store:  # Check if number already exists in the list
        print("The number already exists.")
    else:
        counter += 1  # Increment the counter
        list_store.append(num)  # Add the number to the list

if counter == 10:  # Check if 10 distinct numbers were entered
    print("Here are all the 10 distinct numbers: ")
    print(list_store)
else:
    print("You exited the program.")


        
