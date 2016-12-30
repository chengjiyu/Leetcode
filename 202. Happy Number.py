class Solution(object):
    def squareSum(self, n):
        return sum([int(i) ** 2 for i in str(n)])

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # while n > 6:
        #     s = 0
        #     for i in str(n):
        #         s += int(i)**2
        #     n = s
        # if n == 1:
        #     return True
        # else:
        #     return False
        # 弗洛伊德环检测算法
        slow = fast = n
        while True:
            slow = self.squareSum(slow)
            fast = self.squareSum(fast)
            fast = self.squareSum(fast)
            if slow == fast:
                break
        return slow == 1
        # 利用10以内的happy number只有1和7，或者先求出100以内的所有happy number等。
        happySet = set([1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97])
        while n > 99:
            n = sum([int(i) ** 2 for i in str(n)])
        return n in happySet


