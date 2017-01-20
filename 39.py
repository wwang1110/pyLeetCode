class Solution(object):
    def combinationSum(self, candidates, target):
        def coSum(candidates, idx, target, cobo, res):
            if target == 0:
                res.append(cobo)
                return

            if target < 0 or idx >= len(candidates):
                return

            c = list(cobo)
            t = target
            while t >= 0:
                coSum(candidates, idx+1, t, c, res)
                t -= candidates[idx]
                if t >= 0:
                    c.append(candidates[idx])

        res=[]
        coSum(candidates, 0, target, [], res)
        return res
