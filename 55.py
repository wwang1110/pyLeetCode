class Solution(object):
    def canJump(self, nums):
        if len(nums) == 0:
            return False
        maxjump = 0
        i = 0
        while i <= maxjump and maxjump < len(nums)-1:
            maxjump = max(maxjump, i+nums[i])
            i += 1
        if maxjump >= len(nums)-1:
            return True
        return False
