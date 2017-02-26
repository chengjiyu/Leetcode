# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
# (ie, buy one and sell one share of the stock multiple times). 
# However, you may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        res = 0
        while i<len(prices)-1:
            add = prices[i+1]-prices[i]
            if add > 0:
                res += add
            i += 1
        return res
        
        return sum(max(prices[i+1]-prices[i]) for i in range(len(prices)-1))
            