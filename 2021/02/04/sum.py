s = 0
for i in range(1, 10 + 1):
    s += i
print(s)

s = sum(i for i in range(1, 10 + 1))
print(s)

s = sum(range(1, 10 + 1))
print(s)
