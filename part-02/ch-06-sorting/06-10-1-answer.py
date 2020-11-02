# n 입력
n = int(input())

# 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 정렬
array = sorted(array, reverse=True)

# 출력
for i in array:
    print(i, end=' ')