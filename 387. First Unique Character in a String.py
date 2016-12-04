class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 对出现的字符计数
        # s_1 = collections.Counter(s)
        # for i in s:
        #     if s_1[i] == 1:
        #         return s.index(i)
        #         break
        # return -1

        # 集合遍历更快
        cache = set()

        if s == '':
            return -1
        for item in s:
            if item not in cache:
                if s.count(item) == 1:
                    return s.index(item)
                else:
                    cache.add(item)

        return -1