# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array. 
# For example,
# Given nums = [0, 1, 3] return 2. 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity? 
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)*(len(nums)+1)/2 - sum(nums)
        # These use O(n) extra space, but I like them anyway
        return reduce(operator.xor, nums + range(len(nums)+1))
        # Xor-ing with O(1) space
        # Saw this from ts before. Xoring 0..n results in [n, 1, n+1, 0][n % 4]. 
        # You can also spot the pattern by looking at xors of such ranges, and it's easy to explain as well.
        n = len(nums)
        return reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]
        # Set/array difference
        # Don't know about Ruby's runtime, might not be linear. Python's sets are hash sets and 
        # the difference is linear time on average. Don't know about its worst case, 
        # and apparently neither does the TimeComplexity page.
        return (set(range(len(nums)+1)) - set(nums)).pop()  # ²î¼¯

