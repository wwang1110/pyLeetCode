class Solution(object):
    def plusOne(self, digits):
        d = list()
        fg = 1
        i = len(digits)-1
        while i >= 0:
            s = digits[i] + fg
            d = [s%10] + d
            fg = s // 10
            i -= 1
        if fg > 0:
            d = [fg] + d
        return d
