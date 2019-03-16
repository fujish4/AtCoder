d, g = map(int, input().split())
pc = [0] + [[int(i) for i in input().split()] for i in range(d)]

def dfs(g, d):
    if d == 0:
        return 10 ** 12
    
    n = min(g // (100 * d), pc[d][0])
    score = n * 100 * d
    
    if n == pc[d][0]:
        score += pc[d][1]
        
    if g > score:
        n += dfs(g - score, d - 1)
        
    return min(n, dfs(g, d - 1))

print(dfs(g, d))
