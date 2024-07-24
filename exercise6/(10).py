def maximalSquare(matrix):
    if not matrix:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    dp = [[0]*col for _ in range(row)]
    res = 0
    for i in range(row):
        for j in range(col):
            # 非边缘，最差的情况是四周有0，无法得到更大的正方形，则返回1，matrix[i][j]自己形成一个最小正方形
            # 如果周边最小为1，至少matrix[i][j]可以形成一个边长为2的正方形
            # 以此类推
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
                if dp[i][j] > res:
                    res = dp[i][j]
    return res

print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))