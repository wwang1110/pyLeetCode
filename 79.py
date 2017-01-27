class Solution(object):
    def exist(self, board, word):
        def dfs(board, word, tb, i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or tb[i][j] == 1:
                return False
            if word[idx] == board[i][j]:
                tb[i][j] = 1
                res = False
                res = res or dfs(board, word, tb, i-1, j, idx+1)
                res = res or dfs(board, word, tb, i+1, j, idx+1)
                res = res or dfs(board, word, tb, i, j-1, idx+1)
                res = res or dfs(board, word, tb, i, j+1, idx+1)
                tb[i][j] = 0
                return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    tb = [[0 for x in range(len(board[0]))] for y in range(len(board))]
                    if dfs(board, word, tb, i, j, 0) == True:
                        return True
        return False
