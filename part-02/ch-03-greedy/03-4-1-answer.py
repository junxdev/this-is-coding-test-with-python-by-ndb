n, k = map(int, input().split())
result = 0

# n이 k 이상일 때 계속 나누기
while n >= k:
    # n이 k의 배수가 될 때까지 계속 빼기
    while n % k != 0:
        n -= 1
        result += 1
    n = n // k
    result += 1

# n이 1이 될 때까지 계속 빼기
while n > 1:
    n -= 1
    result += 1

print(result)