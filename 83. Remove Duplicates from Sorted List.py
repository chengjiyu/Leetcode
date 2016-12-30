# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 遍历所有节点，对于每个节点，检查其后的一个节点是否与当前节点值相同，若相同则删除后面的节点。循环下去。
        p = head
        while p:
            if p.next and p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
        # 遍历所有节点，对于每个节点，从后一个节点开始一个个检查是否与当前节点值相同，直到找到一个后面的节点其值与当前节点不同，删除中间的所有与当前节点值相同的节点。循环下去。
        p = q = head
        while p:
            while q and p.val == q.val:
                q = q.next
            p.next = q
            p = q
        return head
        # 递归实现，本质上是从后向前检查是否有相同的节点。
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head if head.val != head.next.val else head.next