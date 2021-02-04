def get_natural_numbers():
    i = 0
    while True:
        i += 1
        yield i


def generator():
    yield 1
    yield 'string'
    yield True


print(get_natural_numbers())

g = get_natural_numbers()
# for _ in range(100):
#     print(next(g))

# for _ in range(100):
#     print(next(g))

g2 = generator()

print(next(g2))
print(next(g2))
print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
