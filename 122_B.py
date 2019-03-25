
S = input()
ans = 0
count = 0

for s in S:
    if s in ["A", "C", "G", "T"]:
        count += 1
        ans = max(ans, count)
    else:
        count = 0

print(ans)