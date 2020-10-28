n = input()
if int(ord(n[1])) > int(ord('8')) or int(ord(n[1])) < int(ord('1')):
    row = int(n[0])
    col = int(ord(n[1])) - int(ord('a')) + 1 
else:
    row = int(n[1])
    col = int(ord(n[0])) - int(ord('a')) + 1 

count = 0

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for i in range(8):
    nx = row + dx[i]
    ny = col + dy[i]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8: continue

    count += 1

print(count)