class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        maxprofit = 0
        minprices = prices[0]
        for i in range(len(prices)):
            # if prices[i] < minprices:
            #     minprices = prices[i]
            # if prices[i] - minprices > maxprofit:
            #     maxprofit = prices[i] - minprices
            minprices = min(minprices, prices[i])
            maxprofit = max(maxprofit, prices[i]-minprices)
        return maxprofit