class Solution(object):
    def subsetsWithDup(self, nums):
        def dfs(nums, tb, res, path, i):
            if i == len(nums):
                res += [path]
                return 
            if i > 0 and nums[i] == nums[i-1] and tb[i-1] == 0:
                dfs(nums, tb, res, path, i+1)
            else:
                tb[i] = 1
                dfs(nums, tb, res, path+[nums[i]], i+1)
                tb[i] = 0
                dfs(nums, tb, res, path, i+1)
        tb = [0 for i in xrange(len(nums))]
        nums.sort()
        res = []
        dfs(nums, tb, res, [], 0)
        return res

