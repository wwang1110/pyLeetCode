class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] > target or matrix[m-1][n-1] < target:
            return False
        j = m * n - 1
        i = 0
        while i < j:
            k = (i + j) // 2
            if matrix[k//n][k%n] < target:
                i = k + 1
            else:
                j = k
        return matrix[i//n][i%n] == target
