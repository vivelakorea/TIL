# https://docs.python.org/3/library/collections.html#collections.defaultdict

from collections import defaultdict, Counter

a = defaultdict(int)
b = 'mississipi'

for k in b:
    a[k] += 1

print(sorted(a.items()))


def constant_factory(value):
    return lambda: value


d = defaultdict(constant_factory('<missing>'))
d.update(name='John', age=30)

print('%(name)s is %(age)d years old and lives in %(place)s ' % d)


a = [1, 2, 3, 4, 4, 4, 3, 3, 3, 3, 6, 7, 7, 7, 7, 6, 6, 6, 0, 9]
b = Counter(a)
print(b)
print(b.most_common(2))
