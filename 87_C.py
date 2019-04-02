N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
sum = 0
 
for i in range(len(A1)-1):
    temp = 0
    for j, (k, l) in enumerate(zip(A1[1:], A2[:-1])):
        if j >= i:
            temp += l
        else: 
            temp += k
    sum = max(sum, temp)
 
print(sum + A1[0] + A2[-1])