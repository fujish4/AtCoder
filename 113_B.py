N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

x = [abs(A - (T-0.006*h)) for h in H]
print(x.index(min(x))+1)