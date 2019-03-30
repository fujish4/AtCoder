a, b, c = map(int, input().split())
count = max(a, b, c)*3 - a - b - c

if count%2 == 0:
    print(count//2)
else:
    print(count//2+2)