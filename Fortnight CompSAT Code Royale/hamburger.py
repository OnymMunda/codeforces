string = input()
n_b, n_s, n_c = map(int, input().split())
p_b, p_s, p_c = map(int, input().split())
rubles = int(input())

max = 0
recipe = {
    "B": 0,
    "S": 0,
    "C": 0
}

for i in range(len(string)):
    if string[i] == "B":
        recipe["B"] += 1
    if string[i] == "S":
        recipe["S"] += 1
    if string[i] == "C":
        recipe["C"] += 1

available = {
    "B": 0,
    "S": 0,
    "C": 0
}

available["B"] = n_b
available["S"] = n_s
available["C"] = n_c

while available["B"] >= recipe["B"] and available["S"] >= recipe["S"] and available["C"] >= recipe["C"] :
    available["B"] -= recipe["B"]
    available["S"] -= recipe["S"]
    available["C"] -= recipe["C"]
    max += 1


if available["B"] < recipe["B"]:
    diff_B = recipe["B"] - available["B"]
    price_B = diff_B * p_b
    if price_B <= rubles:
        rubles -= price_B



