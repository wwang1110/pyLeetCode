class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)

        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1
