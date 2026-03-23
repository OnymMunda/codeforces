t = int(input())

ans = 0

for _ in range(t):
    n = int(input())

    i = 1
    m = 0

    while i <= n: # can do log
        i *= 2
        m += 1


    geom_series = (2**m - 1)
    arith_series = (n * (1+n)) // 2 
    ans = arith_series - (2 *geom_series)

    print(ans)

    
