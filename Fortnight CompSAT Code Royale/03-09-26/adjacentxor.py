t = int(input())

ans = ""
count = 0
stop = 0

for _ in range(t):
    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]

    for i in range(n-1):
        if a[n-1] != b[n-1]:
            break
        if a[i] == b[i]:
            continue
        else:
            if(a[i] ^ a[i+1]) != b[i]:
                count += 1
            elif (a[i] ^ a[i+1] == b[i]):
                a[i] = b[i]
   
    for j in reversed(range(n-2)):
        if a[j] == b[j]:
            continue
        else:
            if(a[j] ^ a[j+1]) != b[j]:
                break
            elif (a[j] ^ a[j+1] == b[j]):
                a[j] = b[j]

    if a == b:
        ans += "YES\n"
    else:
        ans += "NO\n"

print(ans.strip())