# 부품 찾기

# 가게 부품 입력
n = int(input())
parts = list(map(int, input().split()))

# 주문 입력
m = int(input())
orders = list(map(int, input().split()))

import time
start_time = time.time()

for order in orders:
    find = False
    for i in range(n - 1):
        if parts[i] == order:
            find = True
            del parts[i]
            n -= 1
    if find:
        print('yes', end=' ')
    else:
        print('no', end=' ')

end_time = time.time()
print('\n', end_time - start_time)