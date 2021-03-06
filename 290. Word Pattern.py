# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in str.
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
#
# Notes:
# You may assume pattern contains only lowercase letters,
# and str contains lowercase letters separated by a single space
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        return map(words.index, words) == map(pattern.index, pattern)

        return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))

        hashmap = {}
        mapval = {}
        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != words[i]:
                    return False
            elif words[i] in mapval:        # 要保证pattern中的不同字符不能映射到相同的words
                return False
            else:
                hashmap[pattern[i]] == words[i]
                mapval[word[i]] == True
        return True

