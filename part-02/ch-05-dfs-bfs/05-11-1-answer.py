from collections import deque

# n, m 입력
n, m = map(int, input().split())

# 2차원 리스트 맵 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수
def bfs(x, y):
    # 큐 초기화
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 지도를 벗어난 경우
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            # 길인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    # N, M까지의 최단 경로 반환
    return graph[n - 1][m - 1]

print(bfs(0, 0))