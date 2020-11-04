n = int(input())

d = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        d[i] = 0
        continue
    w, x, y, z = n + 1, n + 1, n + 1, n + 1
    w = d[i - 1] + 1
    if i % 2 == 0:
        x = d[i // 2] + 1
    if i % 3 == 0:
        y = d[i // 3] + 1
    if i % 5 == 0:
        z = d[i // 5] + 1

    d[i] = min(w, x, y, z)

print(d[n])