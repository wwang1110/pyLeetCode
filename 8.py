class Solution(object):
    def myAtoi(self, str):
        s = str.strip()
        if s == "":
            return 0
        flag = 1
        i = 0
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            flag = -1
            i += 1
        num = 0
        while i < len(s) and s[i] >= '0' and s[i] <= '9' and num < 0x80000000:
            num = num * 10 + int(s[i])
            i += 1
            
        num = num * flag
        
        if num > 0x7fffffff:
            return 0x7fffffff
        elif num < -0x80000000:
            return -0x80000000
        return num