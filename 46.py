class Solution(object):
    def permute(self, nums):
        def dfs(s, fgs, path, res):
            if len(path) == len(s):
                res.append(path)
                return
            for i in range(len(s)):
                if fgs[i] == False:
                    fgs[i] = True
                    dfs(s, fgs, path+[s[i]], res)
                    fgs[i] = False

        fgs = [False] * len(nums)
        res = []
        dfs(nums, fgs, [], res)
        return res

