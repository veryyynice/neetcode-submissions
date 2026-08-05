class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        #subset = []
        nums = sorted(nums)
        def dfs(i,subset):
            if i > (len(nums)-1):
                res.append(subset.copy())
                return

            subset.append(nums[i])

            dfs(i+1,subset)
            subset.pop()

            while (i <= (len(nums)-2) and nums[i]==nums[i+1]):
                i+=1
            dfs(i+1,subset)

        dfs(0,[])
        return (res)




    #     class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     #time complexity idk
    #     result = []
    #     #base case is we reach the end
    #     subset =[]
    #     def dfs(i):
    #         if i> (len(nums)-1):
    #             #return subset
    #             result.append(subset.copy())
    #             return
    #         dfs(i+1)
    #         subset.append(nums[i])
    #         dfs(i+1)
    #         subset.pop()


    #     dfs(0)
    #     return(result)

