class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = collections.Counter(s)
        l = 0
        f = 0
        l_1 = []
        for i, j in n.items():
            if j % 2 == 0:
                l += j
            # 奇数减1之后变为偶数加到结果
            else:
                f = 1
                l_1.append(j-1)
        return l + sum(l_1) + f