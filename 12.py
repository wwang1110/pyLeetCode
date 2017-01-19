class Solution(object):
    def intToRoman(self, num):
        tb = 'IVXLCDM'
        i = 0
        roman = ''
        while num > 0:
            n = num % 10
            num //= 10
            if n == 9:
                roman = tb[i] + tb[i+2] + roman
            elif n >= 5:
                roman = tb[i+1] + ''.join([tb[i] for j in range(5,n)]) + roman
            elif n == 4:
                roman = tb[i] + tb[i+1] + roman
            else:
                roman = ''.join([tb[i] for j in range(0, n)]) + roman
            i += 2
        return roman
