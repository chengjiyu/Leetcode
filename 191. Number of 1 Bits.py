class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 利用 n&(n-1) 的trick。简单的说，运算 n = n&(n-1) 可以将n最低位的1变成0，这里不证明。循环进行该运算，循环次数就是n的二进制表示中1的个数。
        # count = 0
        # while n:
        #     n &= n-1
        #     count += 1
        # return count
        # 通过移位操作，一位一位的判定是否是数字1。
        # count = 0
        # while n:
        #     count += n&1
        #     n >>= 1
        # return count
        return bin(n).count('1')