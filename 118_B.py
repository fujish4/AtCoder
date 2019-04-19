n, m = map(int, input().split())
food = set(range(1, m+1))

for i in range(n):
    food &= set(list(map(int, input().split()))[1:])

print(len(food))