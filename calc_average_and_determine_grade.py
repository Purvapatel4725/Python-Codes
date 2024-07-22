#Purva Patel #100886734 # Question 3
def calc_average():
    a = int(input("Enter marks out of 100: "))
    b = int(input("Enter marks out of 100: "))
    c = int(input("Enter marks out of 100: "))
    d = int(input("Enter marks out of 100: "))
    e = int(input("Enter marks out of 100: "))
    f = a + b + c + d + e 
    g = f // 5
    print(g)


def determine_grade():
    marks = int(input("Enter marks to convert into grades: "))
    if marks >= 90:
        grade = "A"
    elif 80 <= marks <= 89:
        grade = "B"
    elif 70 <= marks <= 79:
        grade = "C"
    elif 60 <= marks <= 69:
        grade = "D"
    else:
        grade = "Fail"
    print(grade)

calc_average()
determine_grade()