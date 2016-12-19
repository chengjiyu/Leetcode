class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 求对数，然后乘方，判断得数是否相等
        # which givies a result of math.log(243) / math.log(3) = 4.999999999
        # but math.log10(243) / math.log10(3) is just fine with 5.00000000
        # return n > 0 and 3**round(math.log(n ,3)) == n

        # 求对数，然后乘方，判断得数是否相等
        # if n == 1:
        #     return True
        # elif n == 0 or n % 3 > 0:
        #     return False
        # return self.isPowerOfThree(n / 3)

        # 1162261467 is 3^19,  3^20 is bigger than int
        return n > 0 and (3 ** 19 % n == 0)