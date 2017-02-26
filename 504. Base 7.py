# Given an integer, return its base 7 string representation.
# Example 1:
# Input: 100
# Output: "202"

# Example 2:
# Input: -7
# Output: "-10"

# Note: The input will be in range of [-1e7, 1e7]. 
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # if num == 0:
        #     return "0"
        # res = ""
        # n = abs(num)
        # while n:
        #     res = str(n%7) + res
        #     n /= 7
        # return res if num > 0 else "-"+res
        
        if num < 0: return "-"+self.convertToBase7(-num)
        if num < 7: return str(num)
        return self.convertToBase7(num/7)+str(num%7)