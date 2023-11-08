def solution(board):
    answer = 1234
    dp = []

    res = float("-inf")

    for row in range(len(board)):
        for col in range(len(board[0])):
            if row == 0 or col == 0 or board[row][col] == 0:
                res = max(res,board[row][col])
                continue

            board[row][col] = min(board[row - 1][col],board[row][col-1], board[row-1][col-1]) + 1
            res = max(res, board[row][col])

    answer = res*res
    
    return answer

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	
solution(board)