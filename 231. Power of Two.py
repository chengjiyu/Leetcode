class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 2的幂次 x 表示成二进制一定是一个1后面若干个0，那么 x-1 一定是一个0后面若干个1，所以 x & (x-1) = 0 ，非2的幂无法得到0。
        return n > 0 and (n & (n - 1)) == 0

        # 比较直观暴力的想法是，如果每次将这个数除以2没有余数，直到得到数字1，那么这个数就是2的若干次幂
        if n < 1:
            return False
        while n % 2 == 0:
            n /= 2
        return True if n == 1 else False

        # 注意到2的幂次 x 表示成二进制一定是一个1后面若干个0，那么只要计算输入数的二进制表示是否只有一个1即可。
        return n > 0 and bin(n).count('1') == 1