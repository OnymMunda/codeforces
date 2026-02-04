n = int(input())
i = 1
while (i <= n):
    word = input()
    if len(word)<=10:
        print(word)
    else:
        print(word[0] + str(len(word[1:len(word)-1])) + word[len(word)-1])
    i+=1