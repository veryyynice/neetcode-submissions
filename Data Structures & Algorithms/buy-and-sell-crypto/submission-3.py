class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)< 2: return 0 
        res =0 #-inf someday
        l = 0 #min
        #r = 0 #max

        for i in range(len(prices)):
            #if prices[i]-prices[i-1] > res: 
            #   res = #
            curr = prices[i]
            res = max( prices[i]-prices[l],res)
            if curr < prices[l]:
                l = i
            # if curr > prices[r]:
            #     r = i
            
            
        return res
