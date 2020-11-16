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
    elif b < a:
        parent[a] = b

result = []

for _ in range(m):
    f, a, b = map(int, input().split())
    if f == 0:
        union(parent, a, b)
    elif f == 1:
        if find(parent, a) == find(parent, b):
            result.append(1)
        else:
            result.append(0)
            
for i in result:        
    if i == 1:
        print('YES')
    else:
        print('NO')
