n, k = map(int, input().split())
cards = input()

total = 0
needed = 0
cost = {}

for i in range(len(cards)):
    if cards[i] not in cost:
        cost[cards[i]] = 1
    else:
        cost[cards[i]] += 1

sorted = dict(sorted(cost.items(), key = lambda item: item[1], reverse=True))
sorted_arr = list(sorted.values())

for j in range(len(sorted_arr)):
    if k <= sorted_arr[j]:
        total += k ** 2
        break
    else: 
        if needed == 0:
            total += sorted_arr[j] ** 2
            needed = k - sorted_arr[j]
        else:
            if needed <= sorted_arr[j]:
                total += needed ** 2
                break
            else:
                total += sorted_arr[j] ** 2
                needed -= sorted_arr[j]
print(total)

    
    


    
