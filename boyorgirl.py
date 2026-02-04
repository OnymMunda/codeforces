string = input()

characters = set()

for i in range(len(string)):
    characters.add(string[i])

count = len(characters)

if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")