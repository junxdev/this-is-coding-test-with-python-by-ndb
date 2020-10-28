data = input()
row = int(data[1])
col = (ord(data[0]) - ord('a')) + 1

moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, -1), (-2, -2)]

count = 0

for move in moves:
    next_row = row + move[0]
    next_col = col + move[1]

    if next_row >= 1 or next_row <= 8 or next_col >= 1 or next_col <= 8: 
        count += 1  

print(count)