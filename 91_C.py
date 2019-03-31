N = int(input())

red = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: x[1], reverse=True)
blue = sorted([list(map(int, input().split())) for i in range(N)])
ans = 0

for b_x, b_y in blue:
    for r_x, r_y in red:
        if b_x > r_x and b_y > r_y:
            red.remove([r_x, r_y])
            ans += 1
            break

print(ans)