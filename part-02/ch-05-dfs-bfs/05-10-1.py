

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 1
visited[0][0] = True

def dfs(graph, x, y, visited):
    global count, dx, dy

    #print('x: ', x, ',y: ', y, ',visited: ', visited[x][y], ', ice: ',(lambda h: 'yes' if h == 0 else 'no')(graph[x][y]))

    if graph[x][y] == 0:
        if not visited[x][y]:
            count += 1
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1: 
                continue

            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(graph, nx, ny, visited)

for i in range(n):
    for j in range(m):
        dfs(graph, i, j, visited)

print(count)