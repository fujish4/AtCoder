# S = input()
# t = S

# while '01' in t or '10' in t:
#     t= t.replace('01', '').replace('10', '')

# print(len(S) - len(t))

S = input()


print(min(S.count('0'), S.count('1')) * 2)