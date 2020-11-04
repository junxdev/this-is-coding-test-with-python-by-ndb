n = int(input())
k = list(map(int, input().split()))

result = 0

for i in range(2, n):
    k[i] = max(k[i - 2] + k[i], k[i - 1])

print(max(k[n - 2], k[n - 1]))