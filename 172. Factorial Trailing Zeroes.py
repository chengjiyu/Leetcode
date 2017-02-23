# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 所有尾部0可以看成2*5得到，通过计算所有因子中2和5的个数可以知道尾部0的个数。
        # 2个个数是足够的，只需计算5的个数；25=5*5有2个5的因子，125=5*5*5有3个5的因子
        # 例: 计算135！的尾部0的个数，首先135/5=27，说明135以内有27个5的倍数；27/5=5
        # 说明135内有5个25的倍数，5/5=1，说明135内有1个125的倍数，其中有重复计数，
        # 因为25*4结果有2个0，结果135内因子5的个数为27+5+1=33
        res = 0
        while n > 0:
            n /= 5
            res += n
        return res
        # 递归
        retrun 0 if n == 0 else n/5+self.trailingZeroes(n/5)
        num = self.fac(n)
        while num % 10 == 0:
            res += 1
        return res
    def fac(self, n):
        if n == 0:
            return 1
        return n*self.fac(n-1)