class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in dic:
                dic[key] = []
            dic[key] += [s]
        res = []
        for k, p in dic.items():
            res.append(p)
        return res
