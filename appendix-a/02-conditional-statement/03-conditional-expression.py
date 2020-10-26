score = 85
result = 'success' if score > 85 else 'fail'

print(result)

a = [1, 2, 3, 4, 5, 6, 7]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
         result.append(i)

print(result)

result = [i for i in a if i not in remove_set]

print(result)
