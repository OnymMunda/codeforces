n = int(input())
arr = [int(i) for i in input().split()]

sorted_arr = sorted(arr)


l = 0
while l < n and arr[l] == sorted_arr[l]:
    l += 1

if l == n:
    print("yes")
    print("1 1")
else:
    r = n - 1

    while arr[r] == sorted_arr[r]:
        r -= 1
        
    arr[l:r+1] = reversed(arr[l:r+1])

    if arr == sorted_arr:
        print("yes")
        print(l+1, r+1)
    else:
        print("no")

        







        