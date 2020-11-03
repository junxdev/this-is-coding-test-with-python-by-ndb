n, m = map(int, input().split())

array = list(map(int, input().split()))

import time
start_time = time.time()

start = 0
end = max(array)
h = 0

while start <= end:
    mid = (start + end) // 2

    result = 0
    for i in array:
        if i > mid:
            result += (i - mid)

    if result == m:
        h = mid
        break

    if result > m:
        h = mid
        start = mid + 1
    elif result < m:
        end = mid - 1

print(h)

end_time = time.time()
print(end_time - start_time)