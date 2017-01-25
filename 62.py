class Solution(object):
    def uniquePaths(self, m, n):
        if m==0 or n==0:
            return 0
        tb = [[0 for i in range(n)] for j in range(m)]
        tb[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    tb[i][j] += tb[i-1][j]
                if j-1 >= 0:
                    tb[i][j] += tb[i][j-1]

        return tb[m-1][n-1]
