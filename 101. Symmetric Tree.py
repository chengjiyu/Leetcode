# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # recursively
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left and right and left.val == right.val:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        return False
        # # iteratively
        # if root is None:
        #     return True
        # stack = [(root.left, root.right)]
        # while stack:
        #     left, right = stack.pop()
        #     if left is None and right is None:
        #         continue
        #     if left is None or right is None:
        #         return False
        #     if left.val == right.val:
        #         stack.append((left.left, right.right))
        #         stack.append((left.right, right.left))
        #     else:
        #         return False
        # return True