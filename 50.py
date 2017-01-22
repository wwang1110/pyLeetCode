class Solution(object):
    def myPow(self, x, n):
        def dfs(x, n):
            if n == 1:
                return x
            num = 1
            if n % 2 == 1:
                num = x
            d = dfs(x, n//2)
            return num * d * d

        if n == 0:
            return 1
        f = 1
        if n < 0:
            f = -1
            n = -n

        num = dfs(x, n)

        if f < 0:
            num = 1/num

        return num


