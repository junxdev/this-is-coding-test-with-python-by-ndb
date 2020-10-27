# 첫번째 입력
n, m, k = map(int, input().split())

# 두번째 입력
data = list(map(int, input().split()))

# 큰 수 찾기
data.sort()

first = data[n - 1]
second = data[n - 2]

# 계산
result = 0

while True:
    for _ in range(k):
        if m == 0: break
        result += first
        m -= 1
    if m == 0: break
    result += second
    m -= 1

print(result)