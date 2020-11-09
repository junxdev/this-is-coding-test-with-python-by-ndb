# 개선된 데익스트라 알고리즘

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 노드 정보 리스트
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b까지 거리는 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로의 최단 경로는 0으로 설정하고 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 가장 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 처리했던 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 데익스트라 알고리즘 실행
dijkstra(start)    

# 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우 무한 출력
    if distance[i] == INF:
        print(i, "INFINITY")
    else:
        print(i, distance[i])