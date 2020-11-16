n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
    
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

array = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    array.append((cost, a, b))

array.sort()
result = 0
target = 0

for i in range(len(array)):
    cost, a, b = array[i]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        target = cost

print(result - target)