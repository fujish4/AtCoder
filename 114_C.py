N = int(input())
ans = 0

def dfs(n, f1, f2, f3):
    if n > N:
        return
    if f1 and f2 and f3:
        global ans
        ans += 1

    dfs(n*10+7, True, f2, f3)
    dfs(n*10+5, f1, True, f3)
    dfs(n*10+3, f1, f2, True) 

dfs(0, False, False, False)
print(ans)