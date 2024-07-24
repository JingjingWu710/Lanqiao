def numIslands(grid):
    if not grid:
        return 
    def dfs(row,col):
        grid[row][col] = "0"
        for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
            tmp_r = row + i
            tmp_c = col + j
            if 0<=tmp_r<len(grid) and 0<= tmp_c<len(grid[0]) and grid[tmp_r][tmp_c] == "1":
                dfs(tmp_r,tmp_c)
    count = 0        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(i,j)
                count += 1

    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]  
print(numIslands(grid))