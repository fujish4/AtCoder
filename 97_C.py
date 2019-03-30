s = input()
K = int(input())
 
li = sorted(list(set(s)))
result = []

def substring(l):
    result.append(l)
    if len(result) < K:
        for m in li:
            if l+m in s:
                return substring(l+m)
    else:
        pass

for l in li:
    substring(l)

print(result[K-1])