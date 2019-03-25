n, q = map(int, input().split())
s = input()

m = []
total = 0
b = False

for c in s:
    if c == 'A':
        b = True
    elif c == 'C' and b:
        total += 1
        b = False
    else:
        b = False
    m.append(total)

for _ in range(q):
    l, r = map(int, input().split())
    print(m[r-1] - m[l-1])
