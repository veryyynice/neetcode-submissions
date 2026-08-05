class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #nested for loop 
        res = 0
        # l,h = prices[0],prices[1]

        # while

        lowest = prices[0]

        for sell in prices[1:]:
            if (sell-lowest) > res: res = sell-lowest
            if sell < lowest: lowest = sell

        return res