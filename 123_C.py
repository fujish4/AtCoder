import math
n = int(input())
tp = [int(input()) for i in range(5)]
print(math.ceil(n/min(tp)) + 4)