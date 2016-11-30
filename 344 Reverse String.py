class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

        # l = list(s)
        # l.reverse()
        # s_1 = ''.join(l)
        # return s_1

        # return reduce(lambda x,y: y+x, s)