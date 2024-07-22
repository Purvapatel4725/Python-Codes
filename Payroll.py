a = str(input("Enter employee's name: "))
b = int(input("Enter number of hours worked in a week: "))
c = float(input("Enter hourly pay rate: "))
d = float(input("Enter fedral tax witholding rate: "))
e = float(input("Enter state tax witholding rate: "))
f = b*c
g = f*d
h = f*e
i = g + h
print(f"Employee name: {a}")
print(f"Hours worked: {b}")
print(f"Pay rate: ${c}")
print(f"Gross pay: ${f}")
print("Deductions: ")
print(f"\tFedral witholding({d*100}%): ${g}")
print(f"\tState witholding({e*100}%): ${h}")
print(f"\tTotal deduction: ${i}")
print(f"Net Pay: ${f - i}")

