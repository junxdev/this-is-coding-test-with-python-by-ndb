# 피보나치 수열 재귀 함수

# 한번 계산된 결과를 Memoization하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 재귀함수(Top-down dynamic programming)
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있으면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제는 점화식 사용
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

import time
start = time.time()

print(fibo(34))

end = time.time()
print(end - start)