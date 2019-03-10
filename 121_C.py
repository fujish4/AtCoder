N, M = map(int, input().split())
 
drink = []
sum = 0
count = 0
 
for i in range(N):
    A, B = map(int, input().split())
    drink.append([A, B])
 
drink.sort()

for d in drink:
    if count >= M:
        break
    for i in range(d[1]):
        sum += d[0]
        count += 1
        if count >= M:
            break
 
print(sum) 