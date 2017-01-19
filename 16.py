class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        sum = nums[0]+nums[1]+nums[2]
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                n = nums[i]+nums[j]+nums[k]
                if abs(target-sum) > abs(target-n):
                    sum = n
                if n < target:
                    j += 1
                elif n > target:
                    k -= 1
                else:
                    return sum
        return sum


