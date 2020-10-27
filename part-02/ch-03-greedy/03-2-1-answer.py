# 공백을 구분하여 입력 받기
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 큰 수부터 정렬
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)