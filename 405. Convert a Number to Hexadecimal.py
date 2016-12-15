class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 除 16 取余
        if num == 0:
            return str(num)
        if num < 0:
            num = 2 ** 32 + num  # 2**32 = 0x100000000
        # res = ''
        # while num:
        #     s = num % 16
        #     if s >= 10:
        #         s = chr(87+s)
        #     res += str(s)
        #     num /= 16
        # return res[::-1]
        # hex = '0123456789abcdef'
        # while num:
        #     res += hex[num%16]
        #     num /= 16
        # return res[::-1]
        return '%x' % (num)
