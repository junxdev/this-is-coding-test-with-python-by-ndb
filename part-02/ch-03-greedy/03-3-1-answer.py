# 행, 열 입력
n, m = map(int, input().split())

# 데이터 입력 및 계산
result = 0

for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

# 출력
print(result)