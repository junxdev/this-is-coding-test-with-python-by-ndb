n, m = map(int, input().split())

coin = [0] * n
d = [m + 1] * (m + 1)
d[0] = 0

for i in range(n):
    coin[i] = int(input())

for i in range(min(coin), m + 1):
    for c in coin:
        d[i] = min(d[i], d[i - c] + 1)

if d[m] == m + 1:
    print(-1)
else:
    print(d[m])