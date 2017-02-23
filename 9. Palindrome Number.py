# Determine whether an integer is a palindrome. Do this without extra space.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1] # 使用了额外空间
        # 原数字反转一半， 以0结尾的非零数都不是回文数
        if x < 0 or (x!=0 and x%10 == 0):
            return False
        y = 0
        while x > y:
            y = y*10 + x%10
            x /= 10
        return x == y or y/10 == x
        # 将原数字各个数分离，逐个比较最前最后的数字是否相等
        if x < 0:
            return False
        num = 1
        while x/num >= 10:
            num *= 10
        while num:
            right = x%10
            left = x/num
            if left != right:
                return False
            x = (x%num)/10
            num /= 100
        return True