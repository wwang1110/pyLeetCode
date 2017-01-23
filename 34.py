class Solution(object):
    def searchRange(self, nums, target):
        def searchLeft(nums, target, l, r):
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1

            m = (l + r)//2
            if nums[m] < target:
                return searchLeft(nums, target, m+1, r)
            else:
                return searchLeft(nums, target, l, m)

        def searchRight(nums, target, l, r):
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1

            m = (l + r + 1)//2
            if nums[m] > target:
                return searchRight(nums, target, l, m-1)
            else:
                return searchRight(nums, target, m, r)

        if len(nums) == 0:
            return [-1, -1]
        l = searchLeft(nums, target, 0, len(nums)-1)
        r = searchRight(nums, target, 0, len(nums)-1)
        return [l, r]
