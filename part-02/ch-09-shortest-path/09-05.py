INF = (1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
distance[c] = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cities = 0

for i in range(1, n + 1):
    if distance[i] == INF:
        distance[i] = -1
    elif distance[i] == 0:
        continue
    else:
        cities += 1

print(cities, max(distance[1:n + 1]))