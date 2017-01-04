class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and int(math.log(num, 4)) == math.log(num, 4)

        # 若一个整数是4的幂，则其二进制形式具有如下特点：
        # 1. 最高位为1，其余位为0
        # 2. 0的个数为偶数
        # 条件1可以用num & (num - 1) == 0判断, (先判断是否是 2 的 N 次方)
        # 条件2可以用num & 0x55555555 > 0判断, (再将不是 4 的 N 次方的数字去掉)
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 > 0

        # 说明：也是从数学的角度出发，数num是4的阶乘需要满足的条件是
        # 1）(num -1)%3 == 0
        # 2）num & (num-1) == 0
        return num > 0 and (num - 1) % 3 == 0 and num & (num - 1) == 0