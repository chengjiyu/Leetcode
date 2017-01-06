class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 正负号标记法
        # 遍历数组nums，记当前元素为n，令nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        # 再次遍历nums，将正数对应的下标+1返回即为答案，因为正数对应的元素没有被上一步骤标记过。
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index]) # 把num-1当成出现过的索引值，索引值对应列表中的数标记为负数，则正数就是没出现过的 num-1

        return [i + 1 for i, num in enumerate(nums) if num > 0]