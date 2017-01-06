class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # return bin(x^y).count('1')

        x = x ^ y
        count = 0
        while x:
            count += 1
            x &= x - 1
        return count