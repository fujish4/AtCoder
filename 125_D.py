n = int(input())
A = list(map(int, input().split()))
cnt = 0
minus = 0

for a in A:
    if a < 0:
        cnt += 1

if cnt%2 == 0:
    print(sum( [ abs(a) for a in A ] ))
else:
    print(sum( [ abs(a) for a in A ] ) - min([ abs(a) for a in A ] )*2)