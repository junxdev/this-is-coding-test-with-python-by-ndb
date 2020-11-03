def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return None

# 가게 부품 입력
n = int(input())
array = list(map(int, input().split()))

# 이진 탐색을 위한 정렬
array.sort()

# 주문 입력
m = int(input())
x = list(map(int, input().split()))

# 주문 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if binary_search(array, i, 0, n - 1) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')