n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

import time
start_time = time.time()

result = sorted(array, reverse=True)

for i in range(len(result)):
    print(result[i], end=' ')

end_time = time.time()

print(end_time - start_time)