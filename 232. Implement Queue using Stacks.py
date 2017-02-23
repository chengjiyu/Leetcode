# Implement the following operations of a queue using stacks.
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
# 由于栈先进后出和队列先进先出矛盾， 使用2个栈，一个只进行入栈push操作， 一个只进行出栈pop或peek操作
# 当只进行出栈的栈空时， 将另一个栈中的内容push到该栈， 如此拥有了先进先出的特性
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)
    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.outStack.pop()
    def peek(self):
        """
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
    def empty(self):
        """
        :rtype: bool
        """
        return not self.inStack and not self.outStack