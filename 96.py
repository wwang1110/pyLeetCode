class Solution(object):
    def numTrees(self, n):
        tb = [1] * (n+1)
        for i in range(2, n+1):
            sum = 0
            for j in range(i):
                sum += tb[j] * tb[i-j-1]
            tb[i] = sum
        return tb[n]

