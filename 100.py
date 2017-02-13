class Solution(object):
    def isSameTree(self, p, q):
        def dfs(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return dfs(p.left, q.left) and p.val == q.val and dfs(p.right,q.right)

        return dfs(p,q)
