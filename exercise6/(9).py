def maxProduct(nums):
    if len(nums) == 0:
        return
    # memo = []
    # for i in range(0,len(nums)):
    #     if i == len(nums) - 1:
    #         break
    #     max_product = 0
    #     product = 1
    #     for j in range(i,len(nums)):
    #         product *= nums[j]
    #         if product > max_product:
    #             max_product = product
    #     memo.append(max_product)
    # return max(max(nums),max(memo))
    # 暴力解法，超时
    dp = [[0]*2 for _ in range(len(nums))]
    result = nums[0]
    # 储存直到i的最大值和最小值，储存最小值是因为以防前面有乘积是负数，之后遇到负数乘上没准比正数积大
    dp[0][0], dp[0][1] = nums[0], nums[0]
    for i in range(1,len(nums)):
        dp[i][0] = max(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i])
        dp[i][1] = min(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i])
        result = max(result,max(dp[i]))
    return result

# 动态规划都是一看题目写不出，一看答案会做（融化emoji）
nums = [-2,0,-1]
print(maxProduct(nums))
