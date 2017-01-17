class Solution(object):
    def lengthOfLongestSubstring(self, s):
        x = -1
        dic = {}
        maxlen = 0
        for y in range(len(s)):
            if s[y] not in dic:
                dic[s[y]] = 1
            else:
                dic[s[y]] += 1
                
            while dic[s[y]] > 1:
                x += 1
                dic[s[x]] -= 1
            maxlen = max(y-x, maxlen)
        return maxlen

