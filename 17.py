class Solution(object):
    def lcombination(self, digits, i, cstr, r, dic):
        if i == len(digits):
            if len(cstr) != 0:
                r.append(cstr)
        else:
            for c in dic[digits[i]]:
                self.lcombination(digits, i+1, cstr+c, r, dic)

    def letterCombinations(self, digits):
        dic = { '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', '0':' '}
        r = []
        self.lcombination(digits, 0, '', r, dic)
        return r
