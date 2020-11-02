from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

q = deque()

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q.append((0, 0))

while q:
    h = q.popleft()
    x = h[0]
    y = h[1]
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(graph[n - 1][m - 1])

for i in range(n):
    print(graph[i])