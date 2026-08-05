class Solution:
    def rob(self, nums: List[int]) -> int:
#         #tree maze
#         #2 decisions at each step
#         #either rob or skip house
#         #recursion is brute force
#         #max of these 2 + nums[i]
#         #helper i+2 update sum or i+1, dont update sum
#         #base condition 
#         #1,99,1,1,99,1
#         #base case reached end.. return 0

#         #dp solution
#         #[i] = max of previous or previous -1
#         if not nums:
#             return 0
#         if len(nums)==1:
#             return nums[0]
#         if len(nums)==2:
#             return 0
#         if len(nums)==3:
#             return nums[1]
#         #homes 1-(end-1)
#         dp1 = [0]*(len(nums)-1) 
#         #homes 2-end
#         dp2 = [0]*(len(nums)-1)
        
#         dp1[0] = nums[0]
#         dp1[1] = max(nums[0],nums[1])
#         for i in range(2,len(nums)-1):
#             dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])

#         dp2[1] = nums[1]
#         dp2[2] = max(nums[1],nums[2])
#         for i in range(3,len(nums)-1):
#             dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])

#         return max(dp1[len(nums)-2],dp2[len(nums)-2])
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def helper(nums):
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
        return max(helper(nums[:-1]),helper(nums[1:]))