# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        stack= [(root,0)]
        while stack:
            node, curs = stack.pop()
            if node:
                if not node.left and not node.right:
                    curs += node.val
                    if curs == sum:
                        return True
                stack.append((node.left, curs+node.val))
                stack.append((node.right, curs+node.val))
        return False
        # 递归
        if not root:
            return False
        if not root.left and not root.right:
            return True if root.val == sum else False
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)