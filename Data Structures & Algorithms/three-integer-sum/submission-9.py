class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #brute force would be O(n^3)
        #if we sort it first then 
        #[-1,0,1,2,-1,-4]
        #[-4,-1,-1,0,1,2]
        l,r=0,0
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first = nums[i]
            rest = 0-first
 
            l,r=i+1, len(nums)-1
            while l <r:
                if nums[l]+nums[r]==rest:
                    res.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1 
                elif nums[l]+nums[r] > rest:
                    r-=1
                elif nums[l]+nums[r] < rest:
                    l+=1
        return res
            