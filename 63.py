class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid)==0 or len(obstacleGrid[0])==0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        tb = [[0 for i in range(n)] for j in range(m)]
        tb[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    tb[i][j] = 0
                else:
                    if i-1 >= 0:
                        tb[i][j] += tb[i-1][j]
                    if j-1 >= 0:
                        tb[i][j] += tb[i][j-1]

        return tb[m-1][n-1]
