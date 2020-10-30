# n, m 입력
n, m = map(int, input().split())

# 2차원 리스트 맵 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드 방문
def dfs(x, y):
    # 예외처리
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않은 경우
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 노드 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    
    # 방문한 노드인 경우
    return False

# 모든 노드에 대해 실행(0인 주변 노드에 1 대입)
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)