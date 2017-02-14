# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        que = [root, None]
        ret = []
        layer = []
        while len(que) > 1:
            node = que.pop(0)
            if node is None:
                que.append(node)
                ret += [layer]
                layer = []
            else:
                layer += [node.val]
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
        ret +=[layer]
        return ret


