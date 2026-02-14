number = int(input())

exceptions = [11, 12, 13]

if number in exceptions:
    print(f"{number}th")
elif number % 10 == 1:
    print(f"{number}st")
elif number % 10 == 2:
    print(f"{number}nd")
elif number % 10 == 3:
    print(f"{number}rd")
else:
    print(f"{number}th")