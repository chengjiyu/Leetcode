# Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        res = ""
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != str[0][i]:
                    return res
            res += str[0][i]
        return res
        # 先排序
        if not strs:
            return ""
        strs.sort()
        res = ""
        for i in range(len(str[0])):
            if i >= len(strs[-1]) or strs[-1][i] != strs[0][i]:
                return res
            res += strs[0][i]
        return res
        # zip
        if not strs:
            return ""
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:-i]
        return min(strs)