# 행, 열 입력
n, m = map(int, input().split())

# 데이터 입력
tu = []
for _ in range(n):
    temp = list(map(int, input().split()))
    tu.append(temp)

# 데이터 정렬
x = []

for i in range(n):
    tu[i].sort()
    x.append(tu[i][0])

x.sort()

# 출력
print(x[n - 1])