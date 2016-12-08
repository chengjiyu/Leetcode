class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 这里其实利用Python的排序方便了很多，但要注意 sorted(s) 返回的实际上是字符数组，所以上面代码 sorted(s) == sorted(t) 的比较是数组比较而不是字符串比较。
        # return sorted(s) == sorted(t)

        # 统计两个字符串中不同字符出现的次数，通用的方法应该用字典。
        if len(s) != len(t):
            return False
        else:
            alpha = {}
            beta = {}
            for i in s:
                alpha[i] = alpha.get(i, 0) + 1
            for i in t:
                beta[i] = beta.get(i, 0) + 1
            return alpha == beta