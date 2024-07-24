def updateBoard(board, click):
    start_r = click[0]
    start_c = click[1]

    if board[start_r][start_c] == "M":
        board[start_r][start_c] = "X"
        return board
    
    direction = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]

    def dfs(r,c):
        board[r][c] = 0
        for i,j in direction:
            tmp_r = r + i
            tmp_c = c + j
            if 0<=tmp_c<len(board[0]) and 0<=tmp_r<len(board) and board[tmp_r][tmp_c] == "M":
                board[r][c] += 1
        if board[r][c] == 0:
            board[r][c] = "B"
            for i, j in direction:
                if 0<=r+i<len(board) and 0<=c+j<len(board[0]) and board[r+i][c+j] == "E":
                    dfs(r+i,c+j)
        elif board[r][c] > 0:
            board[r][c] = str(board[r][c])
            return

    dfs(start_r,start_c)
    # if board[start_r][start_c] == "B":
    #     for x,y in direction:
    #         r = start_r + x
    #         c = start_c + y
    #         if 0<=c<len(board[0]) and 0<=r<len(board):
    #             dfs(r,c)
    return board


board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
print(updateBoard(board,click))
