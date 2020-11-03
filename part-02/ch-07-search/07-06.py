# 가게 부품 입력
n = int(input())
array = list(map(int, input().split()))

# 주문 입력
m = int(input())
x = list(map(int, input().split()))

data = [0] * (max(array) + 1)

for i in array:
    data[i] += 1

for i in x:
    if data[i] == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')