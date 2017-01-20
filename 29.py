class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 0x7fffffff
        flag = 1
        if dividend < 0:
            flag = -flag
            dividend = -dividend
        if divisor < 0:
            flag = -flag
            divisor = -divisor

        n = 1
        d = divisor
        while d < dividend:
            d = d << 1
            n = n << 1

        s = 0
        while dividend >= divisor:
            if dividend >= d:
                dividend -= d
                s += n
            else:
                d = d>>1
                n = n>>1

        s = s * flag

        if s > 0x7fffffff or s < -0x80000000:
            return 0x7fffffff

        return s


