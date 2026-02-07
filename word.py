word = input()

counter_upper = 0
counter_lower = 0

for i in range(len(word)):
    if word[i].isupper() == True:
        counter_upper += 1
    else:
        counter_lower += 1

if counter_lower > counter_upper or counter_lower == counter_upper:
    word = word.lower()
else:
    word = word.upper()

print(word)