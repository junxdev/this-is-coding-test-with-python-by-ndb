import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한 설정

# 노드, 간선, 시작 노드 입력
n, m, start = map(int, input().split())
# 노드간 정보 리스트 생성
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    # x에서 y로 가는 시간 z
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로의 시간은 0으로 하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리의 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 노드들을 확인
        for i  in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 실행
dijkstra(start)                

# 도달할 수 있는 노드의 개수
count = 0

# 도달할 수 있는 노드 중 가장 먼 노드와의 거리
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(d, max_distance)

# 시작 노드를 제외하여 출력
print(count - 1, max_distance)