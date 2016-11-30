class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # while num // 10:
        #     num = int(reduce(lambda x,y : int(x)+int(y),str(num)))
        # return num

        # 先分析。一个数，假如设为ABCD，则实际上这个数可以表达为num = A*1000+B*100+C*10+D。
        # 可分解为num = (A+B+C+D) + (999*A+99*B+9*C)，因为我们需要求的是A+B+C+D，所以我们可以采用%的方法。
        # 因为(999*A+99*B+9*C)肯定是9的倍数，则 num % 9 = A+B+C+D，如果A+B+C+D>=10，对9取余，可依照刚才的方法继续分析，结果是一样的。
        # 但是，当num = 9时，9 % 9 = 0，不符合题目的要求，所以算法的核心是
        # result = （num - 1）% 9 + 1

        if num == 0:
            return num
        else:
            return (num - 1) % 9 + 1