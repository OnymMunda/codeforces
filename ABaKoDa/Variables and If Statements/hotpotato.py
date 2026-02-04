s = int(input())
e = int(input())
t = int(input())

d = abs(s - e)

if t >= d and (t - d) % 2 == 0:
    print("YES")
else:
    print("NO")
