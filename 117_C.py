n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
diff = []

for (i, j) in zip(x, x[1:]):
    diff.append(j-i)

diff.sort(reverse=True)
print(sum(diff[n-1:]))
