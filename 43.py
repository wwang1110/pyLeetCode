class Solution(object):
    def multiply(self, num1, num2):
        def plus(num1, num2):
            i = len(num1)-1
            j = len(num2)-1
            m = 0
            num = ''
            while i >= 0 or j >= 0 or m > 0:
                s = m
                if i >= 0:
                    s += int(num1[i])
                    i -= 1
                if j >= 0:
                    s += int(num2[j])
                    j -= 1
                m = s // 10
                num = str(s % 10) + num
            return num
        def mul(num, d):
            i = len(num)-1
            m = 0
            n = ''
            while i >= 0 or m > 0:
                s = m
                if i >= 0:
                    s += int(num[i]) * d
                    i -= 1
                m = s // 10
                n = str(s % 10) + n
            return n
        if num1 == '0' or num2 == '0':
            return '0'
        ret = ''
        for i in reversed(range(len(num1))):
            ret = plus(ret, mul(num2, int(num1[i])))
            num2 += '0'
        return ret

