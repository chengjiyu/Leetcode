class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda x, y: x*10+y, digits)
        return [int(i) for i in str(num+1)]