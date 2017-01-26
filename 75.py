class Solution(object):
    def sortColors(self, nums):
        c = [0,0,0]
        for n in nums:
            c[n] += 1
        i = 0
        while i < len(nums):
            if c[0] > 0:
                c[0] -= 1
                nums[i] = 0
            elif c[1] > 0:
                c[1] -= 1
                nums[i] = 1
            elif c[2] > 0:
                c[2] -= 1
                nums[i] = 2
            else:
                break
            i += 1

