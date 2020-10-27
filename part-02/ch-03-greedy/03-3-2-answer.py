# 행, 열 입력
n, m = map(int, input().split())

# 결과 초기화
result = 0

# 데이터 입력
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    # 현재 행에서 가장 작은 수 찾기
    for i in range(m):
        min_value = min(min_value, data[i])
    # 찾은 작은 수 중 가장 큰 수 찾기
    result = max(result, min_value)

# 출력
print(result)