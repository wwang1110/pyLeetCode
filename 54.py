class Solution(object):
    def spiralOrder(self, matrix):
        def dfs(matrix, path, m, n, i):
            if 2*i >= m or 2*i >= n:
                return path
            if n - 2*i == 1:
                for j in range(i, m-i):
                    path += [matrix[j][i]]
                return path
            if m - 2*i == 1:
                for j in range(i, n-i):
                    path += [matrix[i][j]]
                return path
            for j in range(i, n-1-i):
                path += [matrix[i][j]]
            for j in range(i, m-1-i):
                path += [matrix[j][n-1-i]]
            for j in reversed(range(i+1, n-i)):
                path += [matrix[m-1-i][j]]
            for j in reversed(range(i+1, m-i)):
                path += [matrix[j][i]]
            return dfs(matrix, path, m, n, i+1)
            
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        return dfs(matrix, [], len(matrix), len(matrix[0]), 0)