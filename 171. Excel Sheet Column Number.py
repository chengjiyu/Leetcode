class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sum = 0
        # for c in s:
        #     sum = sum*26 + ord(c) - 64 # 64 = ord('A') - 1
        # return sum

        # return reduce(lambda x,y: x*26 + y, map(lambda x:ord(x)-64, s), 0)

        sum = 0
        for c in s:
            sum = sum * 26 + int(c, 36) - 9
        return sum