# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2. 
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
# If it does not exist, output -1 for this number. 
# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
    # For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    # For number 1 in the first array, the next greater number for it in the second array is 3.
    # For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
    # For number 2 in the first array, the next greater number for it in the second array is 3.
    # For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

# Note:
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # 栈stack维护nums的递减子集，记nums的当前元素为n，栈顶元素为top
        # 重复弹出栈顶，直到stack为空，或者top大于n为止
        # 将所有被弹出元素的next greater element置为n
        dmap = {}   # 保存每个数对应之后第一个大于他的数   
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                dmap[stack.pop()] = n
            stack.append(n)
        return [dmap.get(n, -1) for n in findNums]
        
        res = []
        for i in findNums:
            for j in range(nums.index(i), len(nums)):
                if nums[j] > i:
                    res.append(nums[j])
                    break
                elif j == len(nums)-1:
                    res.append(-1)
        return res