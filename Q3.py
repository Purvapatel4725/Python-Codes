#Purva Patel #100886734
def count_unique_chars(String):
    chars = {}
    for i in String:
        if i not in chars:
            chars[i] = 1
    return len(chars)

while True:
    try:
        String = input("type your input here: ")
        count = count_unique_chars(String)
        print(f"The total number of unique characters are: {count}")
    except:
        print("Invalid input")

