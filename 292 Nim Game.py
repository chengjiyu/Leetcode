class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Multiple of 4 can't win
        if n % 4 == 0:
            return False
        else:
            return True