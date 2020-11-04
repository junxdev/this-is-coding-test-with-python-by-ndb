# 피보나치 수열 재귀 함수

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

import time
start = time.time()

print(fibo(34))

end = time.time()
print(end - start)

# Xn = Xn-1 + Xn-2, X1 = 1, X2 = 1