class Solution(object):
    def generateParenthesis(self, n):
        l = []
        def generate(l, p, left, right, n):
            if len(p)==2*n:
                l.append(p)
                return
            if left < n:
                generate(l, p+'(', left+1, right, n)
            if right < left:
                generate(l, p+')', left, right+1, n)
        generate(l, '', 0, 0, n)
        return l
