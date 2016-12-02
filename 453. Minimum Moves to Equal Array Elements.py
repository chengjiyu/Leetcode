class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 一次移动将n - 1个元素加1，等价于将剩下的1个元素减1。

        # 因此累加数组中各元素与最小值之差即可。
        return sum(nums) - min(nums) * len(nums)