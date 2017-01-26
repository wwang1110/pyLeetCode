class Solution(object):
    def subsets(self, nums):
        l = len(nums)
        pw = pow(2, l)
        res = []
        for i in range(pw):
            x = i
            y = 0
            s = []
            while x > 0:
                m = x % 2
                if m > 0:
                    s += [nums[y]]
                x = x >> 1
                y += 1
            res += [s]

        return res



