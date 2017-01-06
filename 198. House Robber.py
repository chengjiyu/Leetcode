class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now
        # 动态规划（Dynamic Programming）
        # 状态转移方程：
        # dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
        # 其中，dp[i]表示打劫到第i间房屋时累计取得的金钱最大值。
        # 时间复杂度O(n)，空间复杂度O(n)
        # size = len(nums)
        # dp = [0]*(size+1)
        # if size:
        #     dp[1] = nums[0]
        # for i in range(2, size+1):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        # return dp[size]

        # odd, even = 0, 0
        # for i in range(size):
        #     if i%2:
        #         odd = max(odd+nums[i], even)
        #     else:
        #         even = max(even+nums[i], odd)
        # return max(odd, even)
