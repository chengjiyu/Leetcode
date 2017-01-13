class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # res = [[1]*(i+1) for i in range(numRows)]

        # for i in range(numRows):
        #     for j in range(1,i):
        #         res[i][j] = res[i-1][j-1]+res[i-1][j]
        # return res
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1]+[0], [0]+res[-1])]
        return res[:numRows]