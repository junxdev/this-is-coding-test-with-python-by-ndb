from collections import deque

n = int(input())

periods = [0] * (n + 1)
pre_courses_count = [0] * (n + 1)
pre_courses = [[] for _ in range(n + 1)]

data = []
for i in range(1, n + 1):
    data = list(map(int, input().split()))

    periods[i] = data[0]
    for j in range(1, len(data) - 1):
        pre_courses[data[j]].append(i)
        pre_courses_count[i] += 1


def ex():
    results = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        results[i] = periods[i]
        if pre_courses_count[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        
        for i in pre_courses[now]:
            pre_courses_count[i] -= 1
            results[i] = max(results[i], periods[i] + results[now])
            
            if pre_courses_count[i] == 0:
                q.append(i)

    print(results)

ex()