n = int(input())

solved = {
    "A": 0,
    "B": 0,
    "K": 0,
    "D": 0
}

for i in range(n):
    string = input()
    for j in range(len(string)):
        if string[j] == "A":
            solved["A"] += 1
        elif string[j] == "B":
            solved["B"] += 1
        elif string[j] == "K":
            solved["K"] += 1
        else:
            solved["D"] +=1

print(solved["A"], solved["B"], solved["K"], solved["D"])