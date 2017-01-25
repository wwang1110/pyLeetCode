class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        tb = [0 for i in range(n)]
        tb[0] = 1
        tb[1] = 2
        for i in range(2, n):
            tb[i] = tb[i-2] + tb[i-1]
        return tb[n-1]
