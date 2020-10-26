
# sum
result = sum([1, 2, 3, 4, 5])

print(result)

# minimum
result = min(7, 3, 5, 2)

print(result)

# maximum
result = max(7, 3, 5, 2)

print(result)

# eval
result = eval('(3 + 5) * 7')

print(result)

# sorted
result = sorted([9, 1, 8, 5, 4])
print(result)

result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)

result = sorted([('john', 1), ('kelly', 2), ('henderson', 3)], key = lambda x : x[1], reverse = True)
print(result)

data = [9, 1, 8, 5, 4]
data.sort()
print(data)
