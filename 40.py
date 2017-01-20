class Solution(object):
    def combinationSum2(self, candidates, target):
        def dfs(candidates, idx, target, path, res):
            if target == 0:
                res.append(path)
                return
            if target < 0 or idx >= len(candidates):
                return
            dfs(candidates, idx+1, target-candidates[idx], path+[candidates[idx]], res)
            i = idx
            while i < len(candidates) and candidates[i] == candidates[idx]:
                i += 1
            dfs(candidates, i, target, path, res)

        res = []
        candidates.sort()
        dfs(candidates, 0, target, [], res)
        return res
