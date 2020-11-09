# 간단한 데익스트라 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한값을 10억으로 설정

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결된 노드에 대한 정보 리스트 생성
graph = [[] for _ in range(n + 1)]
# 방문 확인 리스트 생성
visited = [False] * (n + 1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a부터 b까지 거리는 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중 가장 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 거리가 짧은 노드
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 노드에 대해 반복
    for i in range(n - 1):
        # 방문하지 않은 노드 중 현재 최단 거리가 가장 짧은 노드를 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 데익스트라 알고리즘 실행
dijkstra(start)                

# 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우 무한 출력
    if distance[i] == INF:
        print(i, "INFINITY")
    else:
        print(i, distance[i])