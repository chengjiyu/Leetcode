# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 根据BST的性质，左子树节点的值＜根节点的值，右子树节点的值＞根节点的值
        # 记当前节点为node，从根节点root出发
        # 若p与q分别位于node的两侧，或其中之一的值与node相同，则node为LCA
        # 否则，若p的值＜node的值，则LCA位于node的左子树
        # 否则，LCA位于node的右子树
        # 递归版本
        # if p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # elif p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return root
        # 迭代版本
        while (p.val - root.val) * (q.val - root.val) > 0:
            root = [root.left, root.right][p.val > root.val]
            # 如果p.val > root.val， root = root.right, 判断二叉树是往左子节点还是右子节点走
        return root
