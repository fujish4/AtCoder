n, k = map(int, input().split())
st = input() + "4"
cnt = 1
before = 3
line = []
ans = 0

for s in st:
    if s == before:
        cnt +=1
    else:
        line.append(cnt)
        cnt = 1
        before = s

if st[0] == "1":
    start = 1
else:
    start = 2
    ans = sum(line[1:2*k+1])

for i in range(start, len(line)-2*k):
    ans = max(ans, sum(line[i:i+2*k+1])) 

if n <= k:
    ans = n

print(ans)