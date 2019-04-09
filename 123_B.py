import math
dish = [ int(input()) for i in range(5) ]
sum = sum([ math.ceil(d/10)*10 for d in dish])
mdish = 10

for d in dish:
    if d%10 != 0:
        mdish = min(d%10, mdish)

print(sum + mdish - 10)
