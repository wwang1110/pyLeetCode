class Solution(object):
    def numDecodings(self, s):
        def isValid(s):
            if len(s) == 1:
                return int(s) > 0
            elif len(s) == 2:
                return int(s) >= 10 and int(s) <= 26
            return False
        if len(s) == 0:
            return 0
        tb = [0 for i in xrange(len(s)+2)]
        tb[0] = 1
        tb[1] = 1
        for i in xrange(2, len(s)+2):
            tb[i] = 0
            if isValid(s[i-2:i-1]):
                tb[i] += tb[i-1]
            if i > 2 and isValid(s[i-3:i-1]):
                tb[i] += tb[i-2]
        return tb[len(s)+1]
