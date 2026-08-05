class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy
        #going from back and make goal n-1 if its n>=1

        goal = len(nums)-1

        for i in range (len(nums)-1,-1,-1):
            curr = nums[i]
            if i + curr >= goal:
                goal = i
            
        return goal ==0