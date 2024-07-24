door = []
n, m = map(int,input().split())
door_dic = {}
#建立门的字典，把每个门的两个口分别作为键，这样就可以互通
if m > 0:
    for _ in range(m):
        door = list(map(int,input().split()))
        door_dic[tuple(door[0:2])] = tuple(door[2:])
        door_dic[tuple(door[2:])] = tuple(door[0:2])

# print(door_dic)
def game(n):
    if n == 1:
        return 0
    ans = 0
    dp = [[0]*(n+1) for _ in range(n+1)]
    #思路是先不考虑有门，先把所有格子到右下角的最短距离算出来
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == n and j == n:
                dp[i][j] = 0
                break
            dp[i][j] = abs(i-n) + abs(j-n)
    #讨论有门的情况
    if door_dic:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == n and j == n:
                    break
                #如果刚好落到门上
                if (i,j) in door_dic.keys():
                    dp[i][j] = min(dp[i][j],1+dp[door_dic[(i,j)][0]][door_dic[(i,j)][1]])
                #落到除了门以外的地方，遍历对比走门和不走门的情况
                else:
                    for x, y in list(door_dic.keys()):
                               dp[i][j] = min(
                                   dp[i][j],abs(i-x)+abs(j-y)+1+
                                   dp[door_dic[(x,y)][0]][door_dic[(x,y)][1]]
                                   )

    for i in dp:
        ans += sum(i)
    ans = ans / (n*n)
    return round(ans,2)
        
print(game(n))
