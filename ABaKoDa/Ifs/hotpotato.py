s = int(input())
e = int(input())
t = int(input())

steps = abs(s-e)

#1 step, even time
if steps == 1 and t % 2 == 0:
    print("NO")
# 0 steps, even time
elif steps == 0 and t % 2 == 0:
    print("YES")
# 0 steps, odd time
elif steps == 0 and t % 2 != 0:
    print("NO")
elif  t > steps and t % steps == 0:
    print("YES")
elif t < steps and steps % t == 0:
    print("YES")
else:
    print("NO")