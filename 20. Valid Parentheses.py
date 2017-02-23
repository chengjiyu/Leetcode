# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# The brackets must close in the correct order,
# "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        parmap = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in parmap:
                if parmap[i] != pars.pop():
                    return False
            else:
                pars.append(i)
        return len(pars) == 1