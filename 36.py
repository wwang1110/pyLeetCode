class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j]<'0' or board[i][j]>'9':
                    return False
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])

        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])

        for i in range(9):
            s = set()
            for j in range(9):
                x = (i%3)*3+j%3
                y = (i//3)*3+j//3
                if board[x][y]=='.':
                    continue
                if board[x][y] in s:
                    return False
                else:
                    s.add(board[x][y])

        return True
