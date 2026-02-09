x = int(input())

max_steps = x // 5
remaining = 1 if x % 5 else 0

# if remaining:
#     excess = True
# else:
#     excess = False

# total = max_steps

# if excess:
#     total += 1

# print(total)

print(max_steps + remaining)