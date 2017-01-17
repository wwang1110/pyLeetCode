class Solution(object):
    def reverse(self, x):
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        num = 0
        while x > 0:
            m = x % 10
            x /= 10
            num = num * 10 + m
            if num > 0x7fffffff:
                return 0
        return num * flag

