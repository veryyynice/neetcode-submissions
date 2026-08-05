class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #nested for loop 
        res = 0

        for buy in range(len(prices)):
            for sell in prices[buy+1:]:
                if (sell - prices[buy])> res:
                    res = sell-prices[buy]
        return res