x1 = int(input("insert value x1: "))
x2 = int(input("insert value x2: "))
y1 = int(input("insert value y1: "))
y2 = int(input("insert value y2: "))
x2_x1 = x2 - x1
y2_y1 = y2 - y1
sqarex = (x2_x1)**2
sqarey = y2_y1**2
sqarex_sqarey = sqarex + sqarey
whole_root = sqarex_sqarey**(1/2)
print("Distance = " ,whole_root)