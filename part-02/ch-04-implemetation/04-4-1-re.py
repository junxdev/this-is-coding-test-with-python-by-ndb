# 맵 크기 입력
n, m = map(int, input().split())

# 캐릭터 데이터 입력
x, y, direction = map(int, input().split())

# 맵 데이터를 2차원 배열로 입력
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 방문한 위치를 2차원 배열로 형성. 0은 미방문, 1은 방문을 의미
visited = [[0] * m for _ in range(n)]

# 현재 위치는 방문으로 표시
visited[x][y] = 1

# direction = [0, 1, 2, 3] 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시작하면서 방문했으므로 1부터 시작
count = 1
# 왼쪽으로 회전한 횟수
turn = 0

while True:
    # 바라보는 방향에서 왼쪽으로 회전
    turn_left()

    # 앞 칸의 좌표 계산
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 앞 칸이 맵 밖인 경우
    if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
        turn += 1
        continue

    # 앞 칸이 방문하지 않은 육지인 경우 이동
    if visited[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        visited[x][y] = 1
        count += 1
        turn = 0
        continue
    else:
        turn += 1

    # 네 방향 모두 이미 방문했거나 바다인 경우
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤가 바다인 경우
        if array[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
            turn = 0

print(count)