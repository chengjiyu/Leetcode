class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 将两个数组都统计成dict，再计算交集。
        # return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

        # 用字典统计第一个列表都出现了哪些数及出现的次数，然后顺序遍历第二个列表，发现同时出现的数则加入到结果列表中，同时将第一个列表中相应的出现次数减一。
        l = []
        dict_nums1 = collections.Counter(nums1)
        for i in nums2:
            if i in dict_nums1 and dict_nums1[i] > 0:
                l.append(i)
                dict_nums1[i] -= 1
        return l