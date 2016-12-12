class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # 位运算（Bit Manipulation）

        # 10盏灯泡的燃亮情况可以通过0-1024进行表示，然后计数二进制1的个数即可。

        # 利用位运算将状态拆分为小时和分钟。
        ans = []
        # for i in range(1024):
        #     if bin(i).count('1') == num:
        #         h, m = i >> 6, i & 0x3F
        #         if h < 12 and m < 60:
        #             ans.append('%d:%02d' %(h, m))
        # return ans
        # 枚举小时h和分钟m,然后判断二进制1的个数是否等于num
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == num:
                    ans.append('%d:%02d' % (h, m))
        return ans