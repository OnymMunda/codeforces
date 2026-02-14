D = int(input())
M = int(input())
N = int(input())
K = int(input())

diff = M - N

if diff % K != 0:
    print("NO")
else:
    x = diff // K
    if abs(x) <= D and (D + x) % 2 == 0:
        print("YES")
    else:
        print("NO")
