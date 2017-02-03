class Solution(object):
    def restoreIpAddresses(self, s):
        def isValid(s):
            if len(s) > 3:
                return False
            if len(s) == 2 and int(s) < 10:
                return False
            if len(s) == 3 and (int(s) < 100 or int(s) > 255):
                return False
            return True
        if len(s) > 12 or len(s) < 4:
            return []
        ret = []
        for i in range(1, len(s)):
            for j in range(i+1, len(s)):
                for k in range(j+1, len(s)):
                    s1 = s[:i]
                    s2 = s[i:j]
                    s3 = s[j:k]
                    s4 = s[k:]
                    if isValid(s1) and isValid(s2) and isValid(s3) and isValid(s4):
                        ret += [s1+'.'+s2+'.'+s3+'.'+s4]
        return ret



