S = input()
K = int(input())

a = 0
b = 0

for i in range(len(S)):
    if S[i] == "1":
        a = i+1
    else:
        b = S[i]
        break

if K <= a:
    print(1)
else:
    print(b)
