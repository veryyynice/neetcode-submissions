class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #time complexity idk
        result = []
        #base case is we reach the end
        subset =[]
        def dfs(i):
            if i> (len(nums)-1):
                #return subset
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return(result)

