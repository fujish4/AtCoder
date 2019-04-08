city = [ int(input()) for i in range(5) ]
k = int(input())
if city[4] - city[0] > k:
    print(':(')
else:
    print('Yay!')