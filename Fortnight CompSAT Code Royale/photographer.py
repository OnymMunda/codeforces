n, d = map(int, input().split()) 
a, b = map(int, input().split()) 

counter = 0
customers = []
requests = []

for i in range(1, n + 1):
    x_i, y_i = map(int, input().split())
    total_memory = (a * x_i) + (b * y_i)
    requests.append((total_memory, i))

requests.sort()

for total_memory, i in requests:
    if total_memory > d:
        continue
    d -= total_memory
    counter += 1
    customers.append(i)

print(counter)
print(*customers)
