# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and
# the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.
# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls, lp = len(s), len(p)
        cp = collections.counter(p)
        cs = collections.counter()
        res = []
        # 对s进行滑动每次len(p)长度的字母个数，判断在s中选择的字母是否和p中出现的个数相同
        for i in range(ls):
            cs[s[i]] += 1
            if i >= lp:
                cs[s[i-lp]] -= 1
                if cs[s[i-lp]] == 0:
                    del cs[s[i-lp]]
            if cs == cp:
                res.append(i-lp+1)
        return res
        # 简化时间复杂度为O(n), 字典cp记录组成目标字符串p的anagram,各字符分别缺多少
        # 整数count记录组成目标字符串p一共还缺多少字符
        ls, lp = len(s), len(p)
        count = lp
        cp = collections.Counter(p)
        res = []
        for i in range(ls):
            if cp[s[i]] >= 1:
                count -= 1
            cp[s[i]] -= 1
            if i >= lp:
                if cp[s[i-lp]] >= 0:
                    count += 1
                cp[s[i-lp]] += 1
            if count == 0:
                res.append(i-lp+1)
        return res