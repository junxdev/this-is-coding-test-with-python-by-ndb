n = int(input())

k = list(map(int, input().split()))

# 3  9  3  2  1  9  4  8  3  5  1  3  4
# 3
# 9
# 3+3, 9 = 9
# 9+2, 9 = 11
# 9+1, 11 = 11

d = [0] * n
for i in range(n):
    if i < 2:
        d[i] = k[i]
    else:
        d[i] = max(k[i] + d[i - 2], d[i - 1])

print(d[n - 1])
print(d)