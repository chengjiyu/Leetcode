# Given a string s consists of upper/lower-case alphabets
# and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.
# For example,
# Given s = "Hello World",
# return 5.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 利用内置函数string.rstrip()和string.split()。
        # 先将字符串后面的空格删掉，再按照空格将剩余部分分割
        return len(s.rstrip().split(' ')[-1])
        # 不用内置函数，先删除后面的空格，从后面数非空格字符数
        length, j = 0, len(s)-1
        while j >= 0:
            if s[j] != ' ':
                break
            j = j - 1
        for i in range(j, -1, -1):
            if s[i] == ' ':
                return length
            length += 1
        return length