# 부품 개수 입력
n = int(input())

# 가게에 있는 부품 입력 
array = [0] * 1000001
for i in input().split():
    array[int(i)] = 1

# 주문 입력
m = int(input())
x = list(map(int, input().split()))

# 주문 하나씩 확인
for i in x:
    # 해당 부품 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')