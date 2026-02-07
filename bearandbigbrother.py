a, b = map(int, input().split())

years_passed = 0

while a <= b:
    a *= 3
    b *= 2
    years_passed += 1

print(years_passed)

    