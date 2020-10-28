# n, m 입력
n, m = map(int, input().split())

# 방문한 위치 저장
d = [[0] * m for _ in range(n)]

# x, y, 방향 입력
x, y, direction = map(int, input().split())

# 현재 좌표 방문 처리
d[x][y] = 1

# 맵 전체 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북동남서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 기능
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 구현
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 가보지 않은 칸이면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 가본 칸이거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else: 
            break
        turn_time = 0

print(count)
