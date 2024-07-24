m = 7
n = 3
dp = [[0]*m for _ in range(n)]
for i in range(1,m):
    for j in range(1,n):
        dp[0][i] = 1
        dp[j][0] = 1

for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])