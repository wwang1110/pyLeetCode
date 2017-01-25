class Solution(object):
    def mySqrt(self, x):
        i = 0
        j = x
        while i < j:
            m = (i + j) // 2
            if m*m <= x and (m+1)*(m+1) > x:
                return m
            elif m * m > x:
                j = m
            else:
                i = m + 1
                
        return i

