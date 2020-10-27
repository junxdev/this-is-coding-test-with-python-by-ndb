# 입력 1
n, m, k = map(int, input().split())

# 입력 2
data = list(map(int, input().split()))

# 데이터 정렬
data.sort()

first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

# 계산
result = 0

result += first * count
result += second * (m - count)

# 출력
print(result)