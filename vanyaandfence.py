n, h = map(int, input().split())
print(n + sum([1 for x in input().split() if int(x) > h]))


# arr = []
# w = 0

# inputs = [int(_) for _ in input().split()]

# # inputs = input().split()
# # for i in range(n):
# #     integer = int(inputs[i])
# #     arr.append(integer)

# for j in range(len(arr)):
#     if arr[j] > h:
#         w += 2
#     else:
#         w += 1

# print(w)