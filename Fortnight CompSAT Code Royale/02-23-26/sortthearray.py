n = int(input())
arr = [int(i) for i in input().split()]

l = 1

for i in range(n):
    if arr[i] == l:
        l += 1
        continue
    else:
        l = arr[i]
        