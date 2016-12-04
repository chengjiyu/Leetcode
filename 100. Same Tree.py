# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 递归方法
        # if p and q:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return p == q
        # 非递归方法，使用栈存储节点， 遍历二叉树
        # stack = [(p,q)]
        # while stack:
        #     p,q = stack.pop()
        #     if p == None and q == None:
        #         continue
        #     elif p == None or q == None:
        #         return False
        #     elif p.val == q.val:
        #         stack.append((p.left, q.left))
        #         stack.append((p.right, q.right))
        #     else:
        #         return False
        # return True
        # 非递归方法，使用队列存储节点
        queue = [(p, q)]
        while len(queue) != 0:
            p, q = queue.pop()
            if p == None and q == None:
                continue
            elif p == None or q == None:
                return False
            elif p.val == q.val:
                queue.insert(0, (p.left, q.left))
                queue.insert(0, (p.right, q.right))
            else:
                return False
        return True
