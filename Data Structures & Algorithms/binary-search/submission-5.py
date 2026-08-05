class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        return (self.search_helper(l,r,nums,target))
    def search_helper(self,left,right,nums,target):
        # if (left+1 == right or right-1 == left):
        #     if target != nums[left] and target!= nums[right]: return -1

        midpoint = (left+right)//2
        if nums[midpoint] == target:
            return midpoint
        if left < right:
            if nums[midpoint]<target:
                return (self.search_helper(midpoint+1,right,nums,target))
            elif nums[midpoint] >target:
                return(self.search_helper(left,midpoint-1,nums,target))
        else: return -1