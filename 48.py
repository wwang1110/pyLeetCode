class Solution(object):
    def rotate(self, matrix):
        if matrix is None:
            return
        n = len(matrix[0])
        i = 0
        while n-2*i-1 > 0:
            for k in range(n-2*i-1):
                x = matrix[i][i+k]
                matrix[i][i+k] = matrix[n-1-i-k][i]
                matrix[n-1-i-k][i] = matrix[n-1-i][n-1-i-k]
                matrix[n-1-i][n-1-i-k] = matrix[i+k][n-1-i]
                matrix[i+k][n-1-i] = x
            i += 1
