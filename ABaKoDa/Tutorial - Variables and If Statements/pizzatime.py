from math import pi

k1 = int(input())
d1 = int(input())
k2 = int(input())
d2 = int(input())

def total_surface_area(k, d):
    return ((pi * d ** 2) / 4) * k

maguire = total_surface_area(k1, d1)
holland = total_surface_area(k2, d2)

if maguire > holland:
    print("Maguire's Pizza")
elif maguire < holland:
    print("Holland's Pizza")
else:
    print("Garfield's Lasagna")



