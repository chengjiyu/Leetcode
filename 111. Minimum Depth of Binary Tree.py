# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 一个节点的最小高度不一定是两个子树的最小高度中较小的，
        # 当一个子树为空时，该节点的最小高度等于另一个子树的最小高度
        if root == None:
            return 0
        if not root.left:
            return 1+self.minDepth(root.right)
        elif not root.right:
            return 1+self.minDepth(root.left)
        else:
            return 1+min(self.minDepth(root.left), self.minDepth(root.right))
