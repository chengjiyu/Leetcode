class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # t 变为列表，移除s中的每个字母，剩余一个就是添加的
        # t = list(t)
        # for i in s:
        #     t.remove(i)
        # return(str(t[0]))

        # 分别统计s和t中每个字母出现的次数，不一样的即为所求。
        # collections.Counter(s)：得到每个字符和其出现次数的字典，如{‘g’: 2, ‘m’: 2, ‘r’: 2, ‘a’: 1, ‘i’: 1, ‘o’: 1, ‘n’: 1, ‘p’: 1}
        # dic_t - dic_s： 得到差集，那就只有多出的那一个字符了，如[‘e’, 1]
        # (dic_t - dic_s).keys()： 得到字符 ‘e’
        dict_s = collections.Counter(s)
        dict_t = collections.Counter(t)
        return (dict_t - dict_s).keys().pop()

        # 用异或操作得到该字母
        # return chr(reduce(operator.xor, map(ord, s + t)))
