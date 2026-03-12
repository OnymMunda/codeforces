string = input()
n_b, n_s, n_c = map(int, input().split())
p_b, p_s, p_c = map(int, input().split())
rubles = int(input())

max_burgers = 0

recipe = {
    "B": 0, 
    "S": 0, 
    "C": 0
    }

for ch in string:
    recipe[ch] += 1


available = {
    "B": n_b, 
    "S": n_s, 
    "C": n_c
    }

burger_cost = recipe["B"] * p_b + recipe["S"] * p_s + recipe["C"] * p_c
while True:

    if available["B"] >= recipe["B"]:
        need_B = 0
    else:
        need_B = recipe["B"] - available["B"]

    if available["S"] >= recipe["S"]:
        need_S = 0
    else:
        need_S = recipe["S"] - available["S"]

    if available["C"] >= recipe["C"]:
        need_C = 0
    else:
        need_C = recipe["C"] - available["C"]
   
    cost = need_B * p_b + need_S * p_s + need_C * p_c

    if cost > rubles:
        break

    rubles -= cost
    available["B"] += need_B
    available["S"] += need_S
    available["C"] += need_C

    available["B"] -= recipe["B"]
    available["S"] -= recipe["S"]
    available["C"] -= recipe["C"]

    max_burgers += 1

    if recipe["B"] == 0:
        available["B"] *= 0
    if recipe["S"] == 0:
        available["S"] *= 0
    if recipe["C"] == 0:
        available["C"] *= 0

    if available["B"] == 0 and available["S"] == 0 and available["C"] == 0:
        max_burgers += rubles // burger_cost
        break
    
print(max_burgers)
