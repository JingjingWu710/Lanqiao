def climbStairs(n):
    # 设置base case
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 储存前面的方法数
    res = [0]*(n+1)
    # 先设置好最初的两个
    res[1],res[2] = 1,2
    for i in range(3,n+1):
        res[i] = res[i-1] + res[i-2]
    return res[n]
