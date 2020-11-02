n = int(input())

array = []

for _ in range(n):
    name, score = map(str, input().split())
    array.append((name, int(score)))

import time
start_time = time.time()

def sort_by_score(data):
    return data[1]

result = sorted(array, key=sort_by_score)

for i in range(len(result)):
    print(result[i][0], end=' ')
    
end_time = time.time()

print(end_time - start_time)