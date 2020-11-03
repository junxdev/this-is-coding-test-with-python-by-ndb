array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

target = 4
start = 0
end = len(array) - 1
result = None

while result == None:
    if start > end:
        result = "원소가 없습니다."
        break

    mid = (start + end) // 2

    if array[mid] == target:
        result = mid
    elif array[mid] < target:
        start = mid + 1
    elif array[mid] > target:
        end = mid - 1

print(result + 1, "번 숫자")