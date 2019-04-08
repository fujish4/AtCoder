import math

dish = [ int(input()) for _ in range(5) ]
sum = sum([ math.ceil(d/10)*10 for d in dish])
min = min([d%10 for d in dish])

if min == 0:
    print(sum)
else:
    print(sum + min - 10)
