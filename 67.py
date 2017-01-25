class Solution(object):
    def addBinary(self, a, b):
        i = len(a)-1
        j = len(b)-1
        c = ''
        fg = 0
        while i>=0 or j>=0 or fg>0:
            s = fg
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            fg = s // 2
            s = s % 2
            c = str(s) + c

        return c
