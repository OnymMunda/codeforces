import math

X = int(input())
Y = int(input())

V = Y - X

r = ((3 * V) / (4 * math.pi)) ** (1/3)
diameter = 2 * r

print(f"{diameter:.5f}")
