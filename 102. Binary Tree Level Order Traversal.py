# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #     # dfs recursively
        #     res, level = [], 0
        #     self.dfs(root, level, res)
        #     return res

        # def dfs(self, root, level, res):
        #     if root:
        #         if len(res) < level + 1:
        #             res.append([])
        #         res[level].append(root.val)
        #         self.dfs(root.left, level+1, res)
        #         self.dfs(root.right, level+1, res)

        #     # dfs + stack
        #     res = []
        #     stack = [(root,0)]
        #     while stack:
        #         node, level = stack.pop()
        #         if node:
        #             if len(res) < level + 1:
        #                 res.append([])
        #             res[level].append(node.val)
        #             stack.append([node.right, level+1])
        #             stack.append([node.left, level+1])
        #     return res

        # bfs + queue
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(node.val)
                queue.append([node.left, level + 1])
                queue.append([node.right, level + 1])
        return res