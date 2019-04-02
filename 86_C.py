N = int(input())
place = [[0,0,0]] + [list(map(int, input().split())) for i in range(N)]
 
def canMove():
    for i in range(1, N+1):
        t = place[i][0] - place[i-1][0]
        x = place[i][1] - place[i-1][1]
        y = place[i][2] - place[i-1][2]
        if x + y <= t and (t -x-y)%2 == 0:
            continue
        else:
            return "No"
    return "Yes"
 
print(canMove())