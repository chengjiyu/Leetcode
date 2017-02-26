# Given an array of integers and an integer k,
# find out whether there are two distinct
# indices i and j in the array such that nums[i] = nums[j]
# and the absolute difference between i and j is at most k.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 遍历列表，将元素值当作键，元素下标当作值，放到字典中，
        # 发现重复元素比较下表的差值是否小于k，如果小于则返回True，否则更新字典中该键值为新下标
        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map and i - num_map[nums[i]] <= k:
                return True
            else:
                num_map[nums[i]] = i
        return False
        # 在遍历列表时维护集合， 集合保存当前元素前面k个元素，
        # 每次访问一个元素时判断是否在该集合中出现过
        window = set([])
        for i in range(len(nums)):
            if i > k:
                window.discard(num[i-k-1])
            if num[i] in window:
                return True
            else:
                window.add(nums[i])
        return False
