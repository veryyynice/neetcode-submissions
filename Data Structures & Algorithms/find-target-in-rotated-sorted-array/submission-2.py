class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #return index of target
        #while l < r
        #mid == target
        #target s
        #if arr[mid+1] < arr[mid] -->>> return mid
        
        n = len(nums)

        l, r = 0, n-1
        #search for seperator
        #612345
        #561234
        #456123
        while l<r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r=mid
        pivot = l
        #then search in the 2 subarrays 
        #inside the bin search we can check for target
        def binsearch(l,r,target):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target: return mid
                if nums[mid] < target:
                    l = mid +1
                else:
                    r = mid -1
                
            return -1
        left_subarray = binsearch(0,pivot-1,target)
        right_subarray = binsearch(pivot,n-1,target)
        if left_subarray != -1:
            return left_subarray
        if right_subarray != -1:
            return right_subarray
        return -1
