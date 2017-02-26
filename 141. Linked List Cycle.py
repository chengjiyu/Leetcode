# Given a linked list, determine if it has a cycle in it.
# Follow up:
# Can you solve it without using extra space?
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 倘若不考虑进一步的要求。顺序遍历链表所有节点，若出现重复访问则说明有环，否则说明无环。
        # 这里注意不能用list保存访问过的节点，查找太慢了；
        # 用dict保存还要考虑到键不能是对象，所以这里采取以对象的id作为键的做法。
        # map = {}
        # while head:
        #     if id(head) in map:
        #         return True
        #     else:
        #         map[id(head)] = True
        #     head = head.next
        # return False
        fast =slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False