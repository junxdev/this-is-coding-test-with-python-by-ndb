# n 입력
n = int(input())

# 학생 정보 리스트 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# Key를 이용하여 점수 기준 정렬
array = sorted(array, key=lambda student: student[1])

# 출력
for student in array:
    print(student[0], end=' ')