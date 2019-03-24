S = input()
max_count = 0
count = 0

for s in S:
    if s in ["A", "C", "G", "T"]:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0

print(max_count)