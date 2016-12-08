class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        # 集合查找快，不在集合中的数加到集合中，如果在说明不止一个,或字典
        # s = set()
        # for i in nums:
        #     if i not in s:
        #         s.add(i)
        #     else:
        #         return True
        # return False
        # 计数
        # if nums == []:
        #     return False
        # n = collections.Counter(nums)
        # if max(n.values()) == 1:
        #     return False
        # return True

        # 先将数组进行排序（排序的复杂度），排序后比较每个元素与后一个元素是否相等即可。
        # if len(nums) <= 1:
        #     return False
        # nums.sort()
        # for i in range(0, len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False