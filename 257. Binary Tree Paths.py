# Given a binary tree, return all root-to-leaf paths.
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        # 用栈实现DFS
        res, stack = [], [(root,'')]
        while stack:
            node, curs = stack.pop()
            if node:
                if not node.left and not node.right:
                    res.append(curs+str(node.val))
                stack.append((node.left, curs+str(node.val)+'->'))
                stack.append((node.right, curs+str(node.val)+'->'))
        return res
        # 用队列实现BFS
        res , queue = [], [(root, '')]
        while queue:
            node, curs = queue.pop()
            if node:
                if not node.left and not node.right:
                    res.append(curs+str(node.val))
                queue.insert(0, (node.left, curs+node.val+'->'))
                queue.insert(0, (node.right, curs+node.val+'->'))
        return res
        # 递归实现深度优先遍历算法
        res, path_list = [], []
        self.dfs(root, path_list, res)
        return res
    def dfs(self, root, path_list, res):
        if not root:
            return
        path_list.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(path_list))
        if root.left:
            self.dfs(root.left, path_list, res)
        if root.right:
            self.dfs(root.right, path_list, res)
        path_list.pop()
