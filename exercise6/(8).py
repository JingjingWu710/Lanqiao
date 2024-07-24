grid = [[1,3,1],[1,5,1],[4,2,1]]
row = len(grid)
col = len(grid[0])
# arr = []
dp = [[0 for _ in range(col)] for _ in range(row)]
# def find(x,y,res):
#     if x > row - 1 or y > col - 1:
#         return
#     res += grid[x][y]
#     # print(x,y)
#     find(x+1,y,res)
#     find(x,y+1,res)
#     if x == row - 1 and y == col - 1:
#         arr.append(res)

# find(0,0,0)
# print(arr)

dp[0][0] = grid[0][0]
for i in range(1,col):
    dp[0][i] = dp[0][i-1] + grid[0][i]
for j in range(1,row):
    dp[j][0] = dp[j-1][0] + grid[j][0]

for i in range(1,row):
    for j in range(1,col):
        dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]

print(dp[-1][-1])