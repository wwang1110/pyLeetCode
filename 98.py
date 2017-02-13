class Solution(object):
    def isValidBST(self, root):
        travel = []
        def dfs(node, travel):
            if node is None:
                return
            dfs(node.left, travel)
            travel +=[node.val]
            dfs(node.right, travel)
        dfs(root, travel)

        for i in range(1, len(travel)):
            if travel[i-1] >= travel[i]:
                return False
        return True 

