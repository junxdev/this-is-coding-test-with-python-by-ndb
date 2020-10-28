map_height, map_width = map(int, input().split())
y, x, d = map(int, input().split())

maps = dict()

for i in range(map_height):
    map_data = list(map(int, input().split()))
    for j in range(map_width):
        maps[(i, j)] = map_data[j]

direction = [0, 1, 2, 3]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

count = 1

while True:
    over = True

    for _ in range(len(direction)):
        if d == 0: 
            d = 3
        else:
            d = direction[direction.index(d) - 1]
            
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or ny > map_height - 1 or nx < 0 or nx > map_width - 1:
            continue

        if maps[(ny, nx)] == 0:
            maps[(y, x)] = 1
            y = ny
            x = nx
            count += 1
            over = False
            break
    
    if over:
        break

print(count)