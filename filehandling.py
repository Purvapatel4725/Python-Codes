#Purva Patel #100886734
def main():
    file =  open("inp_file.txt","w")
    file.write("Python is an interpreted, high-level, and general-purpose programming language.")
    file.close()
    Inputfile = input("Enter the input file: ")
    Outputfile2 = input("Enter the output file: ")
    print("displaying the contents of the input file...........")
    print("\n")
    if Inputfile == "inp_file.txt":
        file2 = open("inp_file.txt","r")
        print(file2.read())
    print("\n")
    if Outputfile2 == "out_file.txt":
        try:
            file3 = open("out_file.txt","r")
            file3.write("Hello")
        except:
            print("out_file.txt does not exist.")
    file4 = open("inp_file.txt","r")
    file5 = open("out_file.txt","w")
    print("\n")
    print("####################After copy from input to output file####################")
    print("\n")
    a = 0
    b = 0
    for x in file4:
        file5.write(x)
        a += len(x)
        b += 1
    print(f"{b} line and {a} chars have been copied to the output file")
    file4.close()
    file5.close()
    print("\n")
    print("####################After append to the output file####################")
    print("\n")
    file6 = open("out_file.txt","a")
    file6.write("\nIt was created by Guido van Russum and first released in 1991.")
    file6.close()
    file6 = open("out_file.txt","r")
    c = 0
    d = 0
    addstr = ""
    for x in file6:
        addstr += x
        c += 1
        d += len(x)
    print(f"Updated count of line in the output file is: {c}")
    print(f"Updated count of characters in the output file is:{d}")
    file6.close()
    print("\n")
    print("Displaying the output of the output file.....")
    print("\n")
    file6 = open("out_file.txt","r")
    print(file6.read())
    file6.close()
    



main()