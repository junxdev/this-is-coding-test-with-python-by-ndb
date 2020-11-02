n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

import time
start_time = time.time()

a.sort()
b.sort(reverse=True)

for i in range(k):
    if b[i] > a[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))

end_time = time.time()
print(end_time - start_time)