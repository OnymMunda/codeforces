n, k = [int(i) for i in input().split()]
scores = [int(j) for j in input().split()]

advanced = []

sort_scores = sorted(scores, reverse=True)
kth_score = sort_scores[k-1]

for m in sort_scores:
    if m >= kth_score and m > 0:
        advanced.append(m)

print(len(advanced))

    
