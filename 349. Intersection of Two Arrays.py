class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # s = set()
        # for i in nums1:
        #     if i in nums2:
        #         s.add(i)
        # return list(s)

        # return [i for i in set(nums1) if i in nums2]

        return list(set(nums1) & set(nums2))
