class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [0,1]
        # # we return min cost to escape array so, index n (non existant)
        cache = {}
        # i =0
        n = len(cost)
        def helper(i):
            #always base condition first
            if i>=n:
                return 0
            if i in cache:
                return (cache[i])
            
            cache[i] = cost[i]+min(helper(i+1),helper(i+2))

            return cache[i]
        
        return min(helper(0), helper(1))
             
        # for i in range (len(cost)-3,-1,-1):
            
        #     cost[i] += min(cost[i+1],cost[i+2])

        # return(min(cost[0],cost[1]))

