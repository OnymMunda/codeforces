n = int(input())

res_x = 0
res_y = 0
res_z = 0

for _ in range(n):
    x_i, y_i, z_i = map(int, input().split())

    res_x += x_i
    res_y += y_i
    res_z += z_i

    vectors = {
        "X": res_x,
        "Y": res_y,
        "Z": res_z
    }

if vectors["X"] != 0 or vectors["Y"] !=0 or vectors["Z"] != 0:
    print("NO")
else:
    print("YES")