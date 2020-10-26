i = 1
result = 0

# if i is less than or eqaul to 9, repeat the code below
while i <= 9:
    result += i
    i += 1

print(result)

i = 1
result = 0

# only odd with the condition above
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)
