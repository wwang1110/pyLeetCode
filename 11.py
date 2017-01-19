class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        maxarea = 0
        while i < j:
            h = min(height[i], height[j])
            maxarea = max(maxarea, (j-i)*h)
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return maxarea

