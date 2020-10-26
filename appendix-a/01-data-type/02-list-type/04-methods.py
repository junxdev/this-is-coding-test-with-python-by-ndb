a = [1, 4, 3]
print("default: ", a)

# append
a.append(2)
print("append: ", a)

# sort asc
a.sort()
print("sort asc: ", a)

# sort dsc
a.sort(reverse = True)
print("sort dsc: ", a)

# reverse
a.reverse()
print("reverse: ", a)

# insert
a.insert(2, 3)
print("insert 3 at 2: ", a)

# count
print("count 3: ", a.count(3))

# remove
a.remove(1)
print("removed 1: ", a)

# insert(), remove() take too long
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# only keep values not included in remove_set
result = [i for i in a if i not in remove_set]
print(result)
