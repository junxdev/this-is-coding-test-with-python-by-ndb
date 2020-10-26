result = 0;

for i in range(1, 10):
    result += i

print(result)

# ====================

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print("Student ", i + 1, " has passed the test")

# ====================

cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print("Student ", i + 1, " has passed the test")

# ====================

for i in range(1, 10):
    for j in range(1, 10):
        print(i, ' * ', j , ' = ', i * j)
