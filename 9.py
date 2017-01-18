class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = 0
        innum = x
        while innum > 0:
            m = innum % 10
            innum //= 10
            num = num * 10 + m
            if num > 0x7fffffff:
                return False
        return x == num