N = int(input())
X = list(map(int, input().split()))

temp = X[:]

X.sort()
mi = X[len(X)//2-1]
ma = X[len(X)//2]

for x in temp:
    if x <= mi:
        print(ma)
    else:
        print(mi)