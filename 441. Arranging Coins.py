class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(((1 + 8 * n) ** 0.5 - 1) / 2)

        # k = 0
        # while k*(k+1)/2 <= n:
        #     k += 1
        # return k-1