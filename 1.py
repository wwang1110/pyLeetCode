class Solution(object):
    def twoSum(self, num, target):
        dic = {}
        for idx in range(len(num)):
            n = target - num[idx]
            if n in dic:
                return [dic[n], idx]
            else:
                dic[num[idx]] = idx

        return [0,0]

