a = int(input("Enter the weight in pounds: "))
b = int(input("Enter the height in inches: "))
d = (a/(b*b))*703.069    # 0.453592/0.0254/0.0254 = 703.069
print(f"The BMI is: {d}")
