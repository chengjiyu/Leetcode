class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        # 解法I KMP算法 : 时间复杂度 O(n)
        # 记字符串长度为size
        # 利用KMP算法求next数组，记next数组的最后一个元素为p
        # 若p > 0 并且 size % (size - p) == 0，返回True
        # next数组具有如下性质：
        # str[ 0 : next[i] ] == str[ i + 1 - next[i] : i + 1 ]
        # 例如：
        # a, b, c, d, a, b, c, a, b, c, d, a, b, c, d, c
        # 0, 0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 4, 0
        size = len(str)
        next = [0] * size
        for i in range(1, size):
            k = next[i - 1]
            while str[i] != str[k] and k:
                k = next[k - 1]
            if str[i] == str[k]:
                next[i] = k + 1
        p = next[-1]
        return p > 0 and size % (size - p) == 0

        # 解法II 蛮力法（Brute Force）: 时间复杂度 O(k*n)，其中n是字符串长度，k是n的约数个数
        # 若字符串可以由其子串重复若干次构成，则子串的起点一定从原串的下标0开始
        # 并且子串的长度一定是原串长度的约数
        # 整数约数的个数可以通过统计其质因子的幂得到，而输入规模10000以内整数的约数个数很少
        # 因此通过蛮力法，枚举子串长度即可
        for i in range(1, len(str) / 2 + 1):
            if len(str) % i:
                continue
            if str[:i] * (len(str) / i) == str:
                return True
        return False