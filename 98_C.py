N = int(input())
S = input()

cost = S.count("E")
ans = cost

for s in S:
    if s == "E":
        cost -= 1
        ans = min(ans, cost)
    else:
        cost += 1

print(ans)