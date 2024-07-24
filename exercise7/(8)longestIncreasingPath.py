class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #这道题的思路是，记下从每一格出发的最长递增路径，这样在搜索别的路径时，
        #如果遇到已经有记录最长递增路径的格子，就可以直接加，不需要重复计算
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if memo[row][col] != 0:
                return memo[row][col]
    #考虑最坏的情况，矩阵里没有大于1的递增路径，那么每一格自己就算一个路径
    #所以起码为1
            max_path = 1
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                #深度搜索，因为没有搜索到底就不知道前面是多少
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    max_path = max(max_path, 1 + dfs(new_row, new_col))

            memo[row][col] = max_path
            return max_path
    #不断比较返回值的大小
        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))
        return result