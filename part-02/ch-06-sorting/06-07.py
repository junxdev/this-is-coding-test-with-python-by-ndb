# sort library

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

array.sort()
print(array)

array = [('Banana', 2), ('Apple', 5), ('Carrot', 3)]
def setting(data):
    return data[1]
result = sorted(array, key=setting)
print(result)