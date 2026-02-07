matrix = []

for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] != 1:
            continue
        else:
            i_pos = i
            j_pos = j
            break

steps = abs(i_pos - 2) + abs(j_pos - 2)
print(steps)

