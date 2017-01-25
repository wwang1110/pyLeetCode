class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s)-1
        wlen = 0
        #trim right
        while i >= 0 and s[i] == ' ':
            i -= 1

        #check lenghth
        while i >= 0 and s[i] != ' ':
            wlen += 1
            i -= 1

        return wlen

