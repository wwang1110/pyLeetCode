class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            find = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    find = False
                    break
            if find == True:
                return i
        return -1

