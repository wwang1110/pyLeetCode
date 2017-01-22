class Solution(object):
    def permuteUnique(self, nums):
        def dfs(nums, fgs, path, res):
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if fgs[i] == False:
                    if i > 0 and nums[i-1]==nums[i] and fgs[i-1]==False:
                        continue
                    fgs[i] = True
                    dfs(nums, fgs, path+[nums[i]], res)
                    fgs[i] = False

        nums.sort()
        fgs = [False] * len(nums)
        res = []
        dfs(nums, fgs, [], res)
        return res
