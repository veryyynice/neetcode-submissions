class Solution:
    def climbStairs(self, n: int) -> int:
        # 2 steps: we have 2 ways
        # 3 steps: 2 + 1 = 3 ways
        dp = [0]*n
        if n==1:
            return 1
        if n==2: return 2
        else: 
            dp[1]=2
            dp[2] = 3
            for index in range(3,len(dp)):
                dp[index] = dp[index-1] + dp[index-2]
        print(dp)
        return (dp[n-1])