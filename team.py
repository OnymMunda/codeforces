n = int(input())
i = 1
score = 0
while (i <= n):
    a, b, c = [int(x) for x in input().split()] 
    if (a+b+c) >= 2:
        score += 1
    i+=1
print(score)