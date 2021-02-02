def combination(n, m):
    if (n, m) == (0, 0):
        return 1
    elif n == 0:
        return 0
    elif m == 0:
        return 1
    else:
        return combination(n - 1, m) + combination(n - 1, m - 1)


print(combination(10, 8))
