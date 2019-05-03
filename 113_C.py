n,m=[int(i) for i in input().split()]
id=[[int(i) for i in input().split()]+[j] for j in range(m)]

pre_num=[0]*(n+1)
ans=[""]*m

id.sort(key=lambda x:x[1])

for p, y, i in id:
    pre_num[p] += 1
    ans[i] = str(p).zfill(6) + str(pre_num[p]).zfill(6)

print("\n".join(ans))