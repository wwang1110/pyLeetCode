class Solution(object):
    lstr = ""
    def longestPal(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        if j-i-1 > len(self.lstr):
            self.lstr = s[i+1:j]

    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        for idx in range(len(s)):
            self.longestPal(s, idx, idx)
            self.longestPal(s, idx, idx+1)
        return self.lstr            
