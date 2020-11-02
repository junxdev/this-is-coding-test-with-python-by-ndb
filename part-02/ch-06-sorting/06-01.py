import time
start = time.time()

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 1번부터 순서대로
for i in range(len(array)):
    min_index = i
    # 가장 작은 숫자를 찾은 후
    for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    # 1번과 자리 바꿈
    array[min_index], array[i] = array[i], array[min_index]

print(array)

end = time.time()
print(end - start)