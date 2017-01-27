class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        i = 2
        j = 2
        while j < len(nums):
            if nums[i-2] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

