class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        #brute force for loop then two sum problem with loop skipping over duplicates somehow

        #two pointers
        #4444
        #-4 -1 -1 0 1 2

        for i in range (len(nums)):
            target = 0-nums[i]
            j = i+1
            k = len(nums)-1
            if nums[i] >0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            while j<k:
                curr= nums[i]+nums[j]+nums[k]


                if curr > 0:
                    k-=1
                elif curr < 0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    #k-=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                    #while nums[k] == nums[k+1] and j<k:
                    #    k-=1 
        return (res)
        