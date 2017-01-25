class Solution(object):
    def generateMatrix(self, n):
        def dfs(matrix, n, i, num):
            if 2*i >= n:
                return
            if 2*i + 1 == n:
                matrix[i][i] = num+1
                return
            for j in range(i, n-1-i):
                num += 1
                matrix[i][j] = num
            for j in range(i, n-1-i):
                num += 1
                matrix[j][n-1-i] = num
            for j in reversed(range(i+1, n-i)):
                num += 1
                matrix[n-1-i][j] = num
            for j in reversed(range(i+1, n-i)):
                num += 1
                matrix[j][i] = num
            dfs(matrix, n, i+1, num)
        matrix =[[0 for i in range(n)] for j in range(n)]
        dfs(matrix, n, 0, 0)
        return matrix

