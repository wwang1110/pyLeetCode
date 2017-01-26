class Solution(object):
    def simplifyPath(self, path):
        paths = path.split('/')
        l = list()
        for p in paths:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if len(l) != 0:
                    l.pop()
            else:
                l.append(p)

        res = ''
        for p in l:
            res += '/' + p
        if res == '':
            res = '/'
        return res
