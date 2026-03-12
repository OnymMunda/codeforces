num = int(input())
 
if num < 8:
    print("NO")
elif num % 2 == 0:
    print("YES")
    print(4, num - 4)
else:
    if num == 9 or num == 11:
        print("NO")
    else:
        print("YES")
        print(9, num - 9)