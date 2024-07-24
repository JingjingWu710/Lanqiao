n = int(input())
board = []
for _ in range(n):
    board.append(input().split())

def find(a,b):
    # 出界或者扫描到X或$就停止扫描
    if a < 0 or b < 0 or a >= len(board) or b >= len(board[0]) or board[a][b] != "O":
        return
    else:
        board[a][b] = "$"
    # 上下左右四个方向，进到新的一格它还会再次自动在上下左右搜查
    find(a-1,b)
    find(a+1,b)
    find(a,b-1)
    find(a,b+1)

# 如果board本身怎么样都不能形成包围的结构就直接返回
if len(board) <= 2 or len(board[0]) <= 2:
    return

# 从边缘开始找有没有和边缘连着的O
for i in range(len(board[0])):
    find(0,i)
    find(len(board)-1,i)
for i in range(len(board)):
    find(i,0)
    find(i,len(board)-1)
# 再把$，也就是和边缘连着的O变回O，把没有变成$的O变为X
for i in range(len(board)):
    for j in range(len(board[0])):
        # 我喜欢钱，让它等于美元符号:D
        if board[i][j] == "$":
            board[i][j] = "O"
        elif board[i][j] == "O":
            board[i][j] = "X"
return
# 思路应该是对的，但是不知道为啥最后两个用例通不过
# 输入用例是[["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]




# while True:
#     if len(board) <= 2 or len(board[0]) <= 2:
#         break
#     for i in range(1,len(board)-1):
#         for j in range(1,len(board[0])-1):
#             for k in dir:
#                 dir = [i-1,i+1,-1,1]
#                 if board[]
                # if board[i][j] == "O":
                #     board[i][j] = "X"
                # else:
                #     pass
    # if i == len(board) - 2:
    #     break