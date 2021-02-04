l = list(map(lambda x: x + 10, [1, 2, 3]))
l_ = map(lambda x: x + 10, [1, 2, 3])
print(l, l_)

l2 = [i + 10 for i in [1, 2, 3]]
print(l2)

l3 = [i + 10 for i in [1, 2, 3] if i % 2 == 1]
print(l3)

original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
copy = {key: value for key, value in original.items() if value % 2 == 0}
print(copy)
