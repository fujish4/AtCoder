N = input()
if int(N) % sum(map(int, list(N))) == 0:
    print("Yes")
else:
    print("No")