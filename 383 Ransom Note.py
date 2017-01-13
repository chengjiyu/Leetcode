class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: boolpython
        """
        # 如果ransomNote中的字母在magazine中，移除，不在返回False
        # flag = True
        # m = list(magazine)
        # for i in ransomNote:
        #     if i in m:
        #         m.remove(i)
        #     else:
        #         flag = False
        #         break
        # return flag
        # 统计ransomNote和magazine中每个字母出现的次数，ransomNote的次数小于magazine，返回True
        dict_r = collections.Counter(ransomNote)
        dict_m = collections.Counter(magazine)

        return not (dict_r - dict_m)

        # for i, j in dict_r.items():
        #     if i not in dict_m.keys():
        #         return False
        #     if j > dict_m[i]:
        #         return False
        # return True