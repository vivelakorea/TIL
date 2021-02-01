list1 = [1, 2, 3]
list1[-1]  # 마지막 원소
# JS push == python append
list2 = [4, 5, 6]
list3 = list1 + list2  # [1,2,3,4,5,6]
index = 3
del list3[index]  # pop inside
for index in range(len(list3)):
    print(list3[index])
for index, value in enumerate(list3):
    print(index, value)
# random 모듈:
# ex) random.choice(list3)
# ex) random.randint(start, end) start 이상 end 이하!!!!! 임
# ex) random.shuffle(index3)
# 등등...
dict = {
    'a': 1,
    'b': 2,
}
del dict['a']  # or pop(dict['a'])
print(dict)
print(dict.items(), dict.keys(), dict.values())
for item in dict.items():
    print("{}: {}".format(item[0], item[1]))
dict.clear()
print(dict)

dict1 = {
    'a': 3,
    'b': 4,
}
dict2 = {
    'b': 5,
    'c': 6,
}
dict1.update(dict2)
print(dict1)

a = 1
b = 2
b, a = a, b
print(a, b)

products = {
    '종이': 12,
    '풀': 3,
}

for product in products.items():
    print(product)  # 튜플
    print("{}: {}".format(*product))

# 예외처리 catch 아니고 except
try:
    #1 / 0
    raise StopIteration
except Exception as ex:
    print(ex)

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].

# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

# list.clear()
# Remove all items from the list. Equivalent to del a[:].

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

# list.count(x)
# Return the number of times x appears in the list.

# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

# list.reverse()
# Reverse the elements of the list in place.

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].

# join 순서 JS랑 반대
print(' '.join('a,b,c'.split(',')))

# is(===), isinstance
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2, list1 is list2, isinstance(list1, list))
