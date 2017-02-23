# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character
# while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
# For example,
# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true.
# Note:
# You may assume both s and t have the same length.
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 根据题目映射要求，s有多少种字符，t也有多少种字符。如果将映射写成字符对的形式，
        # 比如('a','c')表示s中字符'a'映射到t中'c'，那么映射的个数与s中字符的种类数相同。
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        # 对于s遍历将其每个字符第一次出现的位置记录成新的数组；对t同样处理。
        return map(s.find, s) == map(t.find, t)
        # 对于s和t分别用一个数组记录每个字符在该字符中上一次出现的位置，同时遍历s和t时，
        # 如果发现他们在某一个位置的字符上次出现的位置不同，返回False
        pos1, pos2 = [-1]*256, [-1]*256
        for i in range(len(s)):
            if pos1[s[i]] != pos2[t[i]]:
                return False
            pos1[ord(s[i])] = pos2[ord(t[i])] = i
        return True
        hashmap = {}
        mapval = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hsahmap[s[i]] != t[i]:
                    return False
            elif t[i] in mapval:
                return False
            else:
                hashmap[s[i]] = t[i]
                mapval[t[i]] = True
        return True