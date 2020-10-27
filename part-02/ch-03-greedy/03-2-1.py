size = 5
count = 8
k = 3
nums = [2, 4, 5, 4, 6]

nums.sort(reverse=True) # 큰 수부터 정렬

result = 0
for i in range(count): # count만큼 더한다
    if i == 0: # 첫 시도는 큰 수
        result += nums[0]
        continue
    if i % k == 0: # 매 k번마다 다음 큰 수
        result += nums[1]
        continue
    result += nums[0]

print(result)