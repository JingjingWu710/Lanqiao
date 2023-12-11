n = input().split()
nums = []
for i in n:
    nums.append(int(i))
nums.sort()
mid = len(nums) // 2
result = 0
# 其实就是每个数和中位数的差的和
for j in nums:
    result += abs(j-nums[mid])
print(result)