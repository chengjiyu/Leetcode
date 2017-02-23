# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 如果只有一个节点，直接返回。否则，将当前链表 a1,a2,...an 的子链表 a2,...an 进行逆转，
        # 返回逆转后的第一个节点的指针，再将 a1 节点加到 a2 节点后面
        # if not head or not head.next:
        #     return head
        # else:
        #     p = head.next
        #     n = self.reverseList(p)
        #     head.next = None
        #     p.next = head
        #     return n
        # 利用栈结构，将链表内容依次压入栈，再从栈依次弹出即可构造逆序。下面的代码用普通数组模拟栈。

        p = head
        newlist = []
        while p:
            newlist.insert(0, p.val)
            p = p.next
        p = head
        for i in newlist:
            p.val = i
            p = p.next
        return head
        # 遍历该单链表，将节点一个一个摘下来，采用 头插法 插入另一条链表： 
        new_head = None  # this is where we build the reversed list (reusing the existing nodes)
        while head:
            temp = head  # temp is a reference to a node we're moving from one list to the other
            head = temp.next  # the first two assignments pop the node off the front of the list
            temp.next = new_head  # the next two make it the new head of the reversed list
            new_head = temp
        return new_head

        new_head = None
        while head:
            head.next, head, new_head = new_head, head.next, head # look Ma, no temp vars!
        return new_head