class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2

            # if l< mid:
            #     l = mid
            # elif (r> mid):
            #     r= mid
            if nums[mid] < nums[r]:
                r = mid
            else: 
                l = mid+1
        return nums[l]
