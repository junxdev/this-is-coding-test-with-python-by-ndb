n = int(input())

d = [0] * (n + 1)

d[1], d[2] = 1, 1

# def fibo(x):
#     if x == 1 or x == 2:
#         return d[x]
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x - 1) + fibo(x - 2)
#     return d[x]

def fibo(x):
    if x == 1 or x == 2:
        return d[x]
    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[x]

print(fibo(n))

# fibo(3) = fibo(1) + fibo(2) = 1 + 1
# fibo(4) = fibo(3) + fibo(2) = fibo(1) + fibo(2) + fibo(2) = 1 + 1 + 1
# fibo(5) = fibo(4) + fibo(3) = (fibo(3) + fibo(2)) + (fibo(2) + fibo(1)) = ((fibo(2) + fibo(1)) + fibo(2)) + (fibo(2) + fibo(1))
# 중복된 계산을 수행하며 시간 증가
# 1, 1, 2, 3, 5, 8, 13, ...