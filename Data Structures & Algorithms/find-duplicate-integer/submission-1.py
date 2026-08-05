class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #n+1 integers
        #ints are >=1 <=n
        #return int that aperas more than once
        #1213
        #0213
        #0013
        #313
        #31-3
        #-31-3

        for i in range(len(nums)):
            curr = nums[i]
            if nums[abs(curr)-1]<0:
                return abs(curr)
            nums[abs(curr)-1]*=-1
        
