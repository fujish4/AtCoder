N, Y = map(int, input().split())

def otoshidama():
    for i in range(N+1):
        for j in range(N+1-i):
            if i * 10000 + j * 5000 + 1000 * (N-i-j) == Y:
                return str(i) + " " + str(j) + " " + str(N-i-j)
    return "-1 -1 -1"

print(otoshidama())
