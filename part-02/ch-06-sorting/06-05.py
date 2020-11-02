import time
start_time = time.time()

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트의 크기가 1 이하면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 기준
    tail = array[1:] # 기준을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽과 오른쪽에서 각각 정렬 및 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

end_time = time.time()
print(end_time - start_time)