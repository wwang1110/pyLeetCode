class Solution(object):
    def convert(self, s, numRows):
        if numRows < 2 or numRows >= len(s):
            return s
        r = [''] * numRows
        m = 2 * numRows - 2
        for i in range(len(s)):
            x = i % m
            if x >= numRows:
                x = m - x
            r[x] += s[i]
        return ''.join(r)
                

