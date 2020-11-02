# 입력
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 오름차순
b.sort(reverse=True) # 내림차순

for i in range(k):
    if b[i] > a[i]: # b가 a보다 클 때 교체
        a[i], b[i] = b[i], a[i]
    else: # a가 b보다 클 때 종료
        break

# 출력
print(sum(a))