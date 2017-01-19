class Solution(object):
    def threeSum(self, nums):
        r = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                n = nums[i]+nums[j]+nums[k]
                if n > 0:
                    k -= 1
                elif n < 0:
                    j += 1
                else:
                    r.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[k-1]==nums[k]:
                        k -= 1
                    while j < k and nums[j+1]==nums[j]:
                        j += 1
                    k -= 1
                    j += 1
        return r

