# 반복문 피노나치 함수

# 계산된 결과를 저장하기 위한 테이블(DP table) 초기화
d = [0] * 100

import time
start = time.time()

def fibo(x):
    i = 1
    j = 1
    k = 1
    for _ in range(x - 2):
        j = i
        i = k
        k = i + j

    return k

print(fibo(99))

end = time.time()
print(end - start)

start = time.time()

# 첫번째, 두번째는 1
d[1] = 1
d[2] = 1
n = 99

# Bottom-up dynamic programming
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
end = time.time()

print(end - start)