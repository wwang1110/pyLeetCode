class Solution(object):
    def minPathSum(self, grid):
        if len(grid)==0 or len(grid[0])==0:
            return 0
        m = len(grid)
        n = len(grid[0])
        tb = [[0 for i in range(n)] for j in range(m)]
        tb[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i-1>=0 and j-1>=0:
                    tb[i][j] = min(tb[i-1][j],tb[i][j-1])+grid[i][j]
                elif i-1>=0:
                    tb[i][j] = tb[i-1][j]+grid[i][j]
                elif j-1>=0:
                    tb[i][j] = tb[i][j-1]+grid[i][j]
        return tb[m-1][n-1]
