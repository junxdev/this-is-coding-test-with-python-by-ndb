# only odds from 0 to 19
array = [i for i in range(20) if i % 2 == 1]

print(array)

# same but long
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

# square number by from 1 to 9
array = [i * i for i in range(1, 10)]

print(array)

# same but long
array = []
for i in range(1, 10):
    array.append(i * i)

print(array)

# N x M two-dimensional list
n = 3
m = 4
array = [[0] * m for _ in range(n)]

print(array)

# same but long
n = 3
m = 4

array = []

for _ in range(n):
    array.append([0] * m)

print(array)

# do not do this
n = 3
m = 4

array = [[0] * m] * n

print(array)

array[1][1] = 5

print(array)
