# Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 将单链表的节点值记录到一个数组内，判断数组是否回文。
        # 时间O(n),空间O(n)
        if not head or not head.next:
            return True
        tmp_list = []
        while head:
            tmp_list.append(head.val)
            head = head.next
        length = len(tmp_list)
        for i in range(0, length/2):
            if tmp_list[i] != tmp_list[length-i-1]:
                return False
        return True
        # 判断回文比较前半部分和后半部分，将前部分压栈，在依次出栈与后半部分比较
        # 时间O(n),空间O(n/2)
        if not head or not head.next:
            return True
        new_list = []
        # 快慢指针法找链表的中点
        slow = fast = head
        while fast and fast.next:
            new_list.insert(0, slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next    # 链表有奇数个节点
        for val in new_list:
            if val != slow.val:
                return False
            slow = slow.next
        return True
        # 判断回文比较前半部分和后半部分,若能将后半部分反转，可以判断回文
        # 时间O(n),空间O(1)
        if not head or not head.next:
            return True
        # 快慢指针法找链表的中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next    # slow指向链表的后半段
        slow = self.reverseList(slow)
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
    def reverseList(self, head):
        new_head = None
        while head:
            temp = head
            head = head.next
            temp.next = new_head
            new_head = temp
        return new_head
