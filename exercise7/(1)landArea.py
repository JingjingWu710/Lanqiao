area = []
n = int(input())
for _ in range(n):
    tmp = list(input().split())
    if "A" in tmp:
        Acol = tmp.index("A")
        Arow = _
    area.append(tmp)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#记录下一个要去的地区
save_step = [(Arow,Acol,0)]
#记录已计算过的地区
dp = [[False]*n for _ in range(n)]
dp[Arow][Acol] = True
def bfs(r,c,step):
    while save_step:
        #按顺序读取第一个路径
        r, c, step = save_step.pop(0)
        print(r,c,step)
        if area[r][c] == "B":
            return step
        #遍历四个方向，符合条件的纳入路径，记录已判断的路径
        for dx, dy in directions:
            nx, ny = r + dx, c + dy
            if 0<=nx<n and 0<=ny<n and dp[nx][ny] == False and area[r][c] != area[nx][ny]:
                save_step.append((nx,ny,step+1))
                dp[nx][ny] = True
    return -1
    
print(bfs(Arow,Acol,0))
                

