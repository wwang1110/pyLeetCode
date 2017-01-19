class Solution(object):
    def romanToInt(self, s):
        num = 0
        dic = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        cur = 0
        for i in reversed(range(len(s))):
            if cur <= dic[s[i]]:
                cur = dic[s[i]]
                num += cur
            else:
                num -= dic[s[i]]
        return num

