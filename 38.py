class Solution(object):
    def countAndSay(self, n):
        def generate(s):
            i=0
            j=0
            r=''
            while i < len(s):
                while i+1 < len(s) and s[i]==s[i+1]:
                    i += 1
                i += 1
                r = r + str(i-j) + s[i-1]
                j = i
            return r
        s=''
        for i in range(n):
            if i == 0:
                s = '1'
            else:
                s=generate(s) 
        return s

