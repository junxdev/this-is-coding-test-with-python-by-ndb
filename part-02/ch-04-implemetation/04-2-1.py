n = int(input())

result = 0

for i in range(n + 1):
    if i == 0: 
        result += 1575
        continue
    if i % 3 == 0:
        result += 3600
        continue
    result += 1575

print(result)
