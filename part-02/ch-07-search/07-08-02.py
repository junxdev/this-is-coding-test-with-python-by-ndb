# 재귀 함수로 구현
def binary(array, target, start, end, height):
    if end < start:
        return height

    mid = (start + end) // 2

    result = 0
    for i in array:
        if i > mid:
            result += i - mid

    if result == target:
        return mid

    if result > target:
        height = mid
        start = mid + 1
        return binary(array, target, start, end, height)
    elif result < target:
        end = mid - 1
        return binary(array, target, start, end, height)

# 데이터 입력
n, m = map(int, input().split())
array = list(map(int, input().split()))

# def lower(h1, h2):
#     h = (h1 + h2) // 2
#     result = sum(map(lambda i: i - h if i > h else 0, array))

#     if result == m or h == h2:
#         return h

#     if result > m:
#         return higher(h, h1)
#     elif result < m:
#         return lower(h, h1)

# def higher(h1, h2):
#     h = (h1 + h2) // 2
#     result = sum(map(lambda i: i - h if i > h else 0, array))

#     if result == m:
#         return h

#     if result > m:
#         return higher(h, h1)
#     elif result < m:
#         return lower(h, h1)

# print(lower(max(array), 0))

# 4 1000000
# 4838843 53495739 999999999 10

import time
start_time = time.time()

print(binary(array, m, 0, max(array), 0))

end_time = time.time()
print(end_time - start_time)