s = input()

x = s[0::2].count("0") + s[1::2].count("1")
y = s[0::2].count("1") + s[1::2].count("0")

print(min(x, y))