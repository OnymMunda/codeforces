n = int(input())

arr = []

for _ in range(n):
    a = input().split()
    t = (a[0], int(a[1]))
    arr.append(t)

sorted_by_score = sorted(arr, key=lambda t: (-t[1], t[0]))

for i in range(n):
    print(f"{sorted_by_score[i][0]} {sorted_by_score[i][1]}")