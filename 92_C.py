n = int(input())
a = [0] + list(map(int, input().split())) + [0]

diff = [abs(i-j) for i, j in zip(a, a[1:])]
sum = sum(diff)

for i in range(n):
    print(sum - diff[i] - diff[i+1] +abs(a[i+2] - a[i]))
