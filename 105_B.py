N = int(input())
for i in range(26):
    for j in range(16):
        if i*4 + j*7 == N:
            print("Yes")
            exit()
print("No")
#