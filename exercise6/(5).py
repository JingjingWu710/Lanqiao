# 荣登最简单一题
def minimumTotal(triangle):
    if len(triangle) <= 1:
        return triangle[0][0]
    dp = [[0]*len(triangle[-1]) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(len(triangle[1])):
        dp[1][i] = dp[0][0] + triangle[1][i]
    if len(triangle) > 2:
        for j in range(2,len(triangle)):
            dp[j][0] = dp[j-1][0] + triangle[j][0]
        for i in range(2,len(triangle)):
            dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
        for i in range(2,len(triangle)):
            for j in range(1,len(triangle[i])):
                if j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                    break
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
    # print(dp)
    return min(dp[-1])

t = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(t))
