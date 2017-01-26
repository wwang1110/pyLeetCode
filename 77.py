class Solution(object):
    def combine(self, n, k):
        def dfs(n, k, path, i, res):
            if len(path) == k:
                res += [path]
                return
            for j in range(i+1, n+1): 
                dfs(n, k, path+[j], j, res)

        res = []
        dfs(n, k, [], 0, res)
        return res
