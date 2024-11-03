import math

n = 62615533
e = 31

print(f"Given n = {n}")

p, q = None, None
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:  # If i divides n, it is a factor
        p, q = i, n // i
        break

print(f"Found factors: p = {p}, q = {q}")
