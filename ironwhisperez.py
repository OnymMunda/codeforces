P = input()
n = int(input())

max_possibility = 2 ** n
digits_left = n-3

duplicates = 0



if n > 5 and n % 3 == 0:
    duplicates = 1 + ((n // 3) - 1)
else:
    duplicate_space = n-6




final = max_possibility - (2 ** digits_left) * (n-2) + duplicates