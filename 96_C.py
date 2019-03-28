def isDraw(s, H, W):
    for h in range(H):
        for w in range(W):
            if s[h][w] != "#":
                continue
            if h > 0 and s[h-1][w] == "#":
                continue
            if h < H-1 and s[h+1][w] == "#":
                continue
            if w > 0 and s[h][w-1] == "#":
                continue
            if w < W-1 and s[h][w+1] == "#":
                continue
            return "No"
    return "Yes"
 
H, W = map(int, input().split())
s = []
 
for i in range(H):
    s.append(input())