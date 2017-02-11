class Solution(object):
    def inorderTraversal(self, root):
        def dfs(node, ret):
            if node is None:
                return
            dfs(node.left, ret)
            ret += [node.val]
            dfs(node.right, ret)
        ret = []
        dfs(root, ret)
        return ret
