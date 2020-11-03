def search(x, array, start, end):
    middle = int((start + end) / 2)

    if x < array[middle]:
        end = middle - 1
        return search(x, array, start, end)
    elif x > array[middle]:
        start = middle + 1
        return search(x, array, start, end)
    elif x == array[middle]:
        return middle + 1

array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

x = search(4, array, 0, len(array) - 1)

print(x)