# 이진 탐색 재귀 함수

# 재귀 함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾으면 중간점 index 반환
    if array[mid] == target:
        return mid
    # 중간점보다 작은 경우
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

# n, target
n, target = list(map(int, input().split()))

# list
array = list(map(int, input().split()))

# 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 없습니다.")
else:
    print(result + 1)