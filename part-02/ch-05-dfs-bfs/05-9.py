from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # queue가 빌 때까지 반복
    while queue:
        # queue에서 원소 추출
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소의 인근 노드 중 방문하지 않은 노드를 queue에 추가하고 방문 처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 2차원 리스트 초기화
graph = [
    [], 
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

# 각 노드 방문 정보 1차원 리스트 초기화
visited = [False] * 9

bfs(graph, 1, visited)