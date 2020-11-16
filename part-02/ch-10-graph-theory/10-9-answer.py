from collections import deque
import copy

# 노드 개수 입력
v = int(input())
# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v + 1)
# 그래프 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프 정보 입력
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 처음 시작
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지
    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            # 해당 원소와 연결된 노드의 진입차수 1 빼기
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

        # 결과 출력
        for i in range(1, v + 1):
            print(result[i])

topology_sort()