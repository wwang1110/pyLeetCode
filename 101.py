# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        def dfs(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)
        if root is None:
            return True
        return dfs(root.left, root.right)

