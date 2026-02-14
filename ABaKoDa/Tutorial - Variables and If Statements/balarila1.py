dlrst = ["d", "l", "r", "s", "t"]
patinig = ["a", "e", "i", "o", "u"]
pb = ["p", "b"]

salita = input()

if salita[0] in dlrst:
    print(f"pan{salita}")
elif salita[0] in pb:
    print(f"pam{salita}")
elif salita[0] in patinig:
    print(f"pang-{salita}")
else:
    print(f"pang{salita}")