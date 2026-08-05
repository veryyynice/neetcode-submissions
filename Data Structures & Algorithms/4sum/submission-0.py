class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #no duplicates we skip dupicates with while loop 
        #for for while for 
        
        #four sum is just 3 threesum with extra for loop after the first for loop in 3 sum
        nums.sort()
        #quad is curr quad
        ans, quad = [],[]
        def kSum(k, start,target):
            if k!= 2: #non base case
                for i in range(start,len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
    
                    kSum(k-1,i+1,target-nums[i])
                    quad.pop()
                return
            #k = 2
            #base case, 2 sum II
            l, r = start, len(nums)-1
            while l<r:
                if (nums[l] + nums[r])<target:
                    l+=1
                elif(nums[l] + nums[r])>target: 
                    r-=1
                else: 
                    ans.append(quad +[nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        kSum(4,0,target)
        return ans

