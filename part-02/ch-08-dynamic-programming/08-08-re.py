n, m = map(int, input().split())

d = [m + 1] * (m + 1)
d[0] = 0

coins = [0] * n
for i in range(n):
    coins[i] = int(input())

for i in range(m + 1):
    for coin in coins:
        if i - coin < 0: 
            continue

        d[i] = min(d[i], d[i - coin] + 1)

if d[m] == m + 1:
    print(-1)
else:
    print(d[m])