p1 = input()
amt1 = int(input())
p2 = input()
amt2 = int(input())
p3 = input()
amt3 = int(input())

prizes = [(amt1, p1), (amt2, p2), (amt3, p3)]

prizes.sort(reverse=True)
 
if prizes[0][0] > (prizes[1][0] + prizes[2][0]):
    print("YES")
    print(prizes[0][1])
else:
    print("NO")
