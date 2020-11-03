n, m = map(int, input().split())
array = list(map(int, input().split()))

h = max(array)
x = 0

while x < m:
    h -= 1
    x = sum(map(lambda i: i - h if i > h else 0, array))

print(h)