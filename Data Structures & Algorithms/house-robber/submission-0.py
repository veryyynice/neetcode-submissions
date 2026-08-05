class Solution:
    def rob(self, nums: List[int]) -> int:
        #tree maze
        #2 decisions at each step
        #either rob or skip house
        #recursion is brute force
        #max of these 2 + nums[i]
        #helper i+2 update sum or i+1, dont update sum
        #base condition 
        #1,99,1,1,99,1
        #base case reached end.. return 0

        #dp solution
        #[i] = max of previous or previous -1
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[len(nums)-1]