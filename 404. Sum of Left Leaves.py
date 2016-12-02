# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
# 大体上分为判断有没有左节点和有没有右节点。
# 如果有左节点，看左节点有没有子节点，没有（即左叶子节点）则直接用起值去加，有则继续对左节点递归。
# 如果有右节点，且右节点有子节点，则对右节点递归，否则不管是没有右节点还是右节点没有子节点（即右叶子节点）都直接看做加0。
# 需要注意的是如果本身节点自己是null，要返回0。另外如果只有根节点自己，也要返回0，
# 因为题目说的是左叶子节点，根节点是不算的。最后要注意的就是在判断所有节点的子节点或者值之前，要对该节点本身是否为null做出判断，否则会有错误的。
        n = 0
        if root:
            if root.left and (root.left.left or root.left.right) is None:   # 左节点没有左子节点和右子节点
                n += root.left.val
            n += self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        return n