N = int(input())
A = list(map(int, input().split()))

i = 1
ai = []
for a in A:
    ai.append(a + i)
    i += 1

