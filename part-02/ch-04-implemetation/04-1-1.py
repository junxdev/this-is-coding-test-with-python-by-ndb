# 데이터 입력
n = input()
move = list(map(str, input().split()))

# 출발지점 초기화
point = [1, 1]

# 이동 기능
def left(point):
    if point[1] == 1: return
    else: point[1] -= 1

def right(point):
    global n
    if point[1] == n: return
    else: point[1] += 1

def up(point):
    if point[0] == 1: return
    else: point[0] -= 1

def down(point):
    global n
    if point[0] == n: return
    else: point[0] += 1

# 실행
for i in range(len(move)):
    if(move[i] == 'L'): left(point)
    elif(move[i] == 'R'): right(point)
    elif(move[i] == 'D'): down(point)
    elif(move[i] == 'U'): up(point)

# 출력
print(point[0], point[1])