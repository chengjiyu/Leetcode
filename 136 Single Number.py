class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # 1.排序；2.每两个数比较不同输出前一个数；3.找不到输出最后一个数
        # n = sorted(nums)
        # if len(n) == 1:
        #     return n[0]
        # else:
        #     for i in range(0,len(n)-1,2):
        #         if n[i] != n[i+1]:
        #             return n[i]
        #     else:
        #         return n[-1]
        # 异或
        result = 0
        for i in nums:
            result ^= i
        return result