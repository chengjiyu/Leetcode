# Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100".
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 利用Python的进转换函数， 先转换为10进制，再把和转换为2进制，
        # 忽略了可能的大数相加细节(Python自己处理)
        return bin(int(a, 2)+int(b, 2))[2:]
        # 从俩个字符的最低位开始，一位一位的2进制相加，并保存进位
        res = ''
        i, j, plus = len(a)-1, len(b)-1, 0
        while i>= 0 or j>=0 or plus == 1:
            plus += int(a[i]) if i>=0 else 0
            plus += int(b[j]) if j>=0 else 0
            res = str(plus%2) + res
            i, j, plus = i-1, j-1, plus/2
        return res
    # 递归
        if not a or not b:
            return a if a else b
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1')+'0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1])+'0'
        else:
            return self.addBinary(a[:-1], b[:-1])+'1'
