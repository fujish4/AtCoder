from itertools import accumulate
 
n, k = list(map(int, input().split()))
s = input()
 
def solve():
    l = []
    prev = '1'
    cnt = 0
    for c in s:
        if prev == c:
            cnt += 1
        else:
            l.append(cnt)
            cnt = 1
        prev = c
    l.append(cnt)
    if prev == '0':
        l.append(0)
 
    w = 2 * k + 1
 
    if len(l) <= w:
        return n
 
    acc = [0] + list(accumulate(l))
    ans = 0
    for i in range(0, len(l) - w + 1, 2):
        ans = max(ans, acc[i + w] - acc[i])
    return ans
 
 
print(solve())