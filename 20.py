class Solution(object):
    def isValid(self, s):
        l = list()
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                l.append(s[i])
            else:
                if len(l) == 0:
                    return False
                item = l.pop()
                if s[i]==')' and item=='(' or s[i]=='}' and item=='{' or s[i]==']' and item=='[':
                    continue
                else:
                    return False
        return len(l)==0
