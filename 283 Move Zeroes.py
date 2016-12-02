class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 但是找到不是0的直接和前面的交换，这样后面的就自动都是0了，不需要再赋值一遍了
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1