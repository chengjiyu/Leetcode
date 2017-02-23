# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# Note: The sequence of integers will be represented as a string.
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n-1):
            res = ''.join([str(len(list(group)))+digit for digit, group in itertools.groupby(res)])
        return res

        res = '1'
        for i in range(n-1):
            new_res, pre, count = '', res[0],0
            for j in range(len(res)):
                if res[j] == pre:
                    count += 1
                else:
                    new_res += str(count)+pre
                    count = 1
                    pre = res[j]
            res = new_res+str(count)+pre
        return res
