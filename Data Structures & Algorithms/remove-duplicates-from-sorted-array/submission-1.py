class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #you could just use sorted set for keeping the order but thats O(nlogn)
        n = len(nums)
        l = r= 0
        #we swap values as to have the unique ones on the left
        while r< n:
            nums[l] = nums[r]
            while r<n and nums[r] == nums[l]:
                r+=1
            l+=1
        return l 