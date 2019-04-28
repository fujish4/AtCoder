def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
 
N = int(input())
A = list(map(int, input().split()))

L = [0, 0]
for ai in A:
    L.append(gcd(L[-1], ai))

R = [0, 0]
for ai in A[::-1]:
    R.append(gcd(R[-1], ai))
 
print(max(gcd(l, r) for l, r in zip(L, reversed(R))))
