class Solution(object):
    def maxSubArray(self, nums):
        if nums is None:
            return 0
        mm = nums[0]
        cm = nums[0]
        i = 0
        j = 1
        while j < len(nums):
            if cm <= 0:
                if cm < nums[j]:
                    mm = max(mm, nums[j])
                    cm = nums[j]
                i = j
            else:
                if cm + nums[j] <= 0:
                    cm = nums[j]
                    i = j
                else:
                    cm += nums[j]
                    mm = max(mm, cm)
            j += 1

        return mm
                    
