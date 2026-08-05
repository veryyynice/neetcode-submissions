class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #
        res =[]
        #nums.sort()

        def helper(i, total, current_nums):
            if total == target:
                res.append(current_nums.copy())
                return 
            # for j in range (i, len(nums)):
            if total > target or i >= len(nums):
                return

            current_nums.append(nums[i])
            helper(i,total+nums[i], current_nums)
            current_nums.pop()
            helper(i+1,total,current_nums)            

        helper(0,0,[])
        return(res)
