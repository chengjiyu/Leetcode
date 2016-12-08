class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = collections.Counter(nums)
        for i, j in n.items():
            if j > len(nums)/2:
                return i
