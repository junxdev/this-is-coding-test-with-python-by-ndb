# 입력 1
n, m, k = map(int, input().split())

# 입력 2
data = list(map(int, input().split()))

# 데이터 정렬
data.sort()

first = data[n - 1]
second = data[n - 2]

big = first * k + second
big_size = k + 1

# 계산
result = big * (m // big_size) + first * (m % big_size)

# 출력
print(result)