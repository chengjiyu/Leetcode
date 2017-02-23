# Given a sorted array, remove the duplicates in place such that 
# each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example,
# Given input array nums = [1,1,2],
# Your function should return length = 2,
# with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len([k for k, g in itertools.groupby(nums)])

        count = 1
        for key, group in itertools.groupby(nums):
            count += 1
        return count

        res = len(nums)
        if res == 0:
            return 0
        index = 0
        for i in range(1,res):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        nums = nums[:index+1]
        return len(nums)

        nums = list(set(nums))
        nums.sorted()
        return len(nums)