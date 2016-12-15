class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 模拟大数加法，注意进位即可。
        result = []
        carry = 0
        l1, l2 = len(num1), len(num2)
        while l1 or l2 or carry:
            s = carry
            if l1:
                l1 -= 1
                s += int(num1[l1])
            if l2:
                l2 -= 1
                s += int(num2[l2])
            carry = s > 9
            result.append(str(s%10))
        return ''.join(result[::-1])