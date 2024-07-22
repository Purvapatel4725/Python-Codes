a = int(input("Enter any number between 0 and 1000: "))
e = a%10
b = (a//10)%10
c = a//100
d = a//1000
f = e + b + c + d
print(f"The sum of the digit is {f}")