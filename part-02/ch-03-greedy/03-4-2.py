# 데이터 입력
n, k = map(int, input().split())

count = 0

while n >= k:
    if n % k != 0:
        count += n - (n // k) * k
    n = n // k
    count += 1

if n > 1: count += n - 1

print(count)