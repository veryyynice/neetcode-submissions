class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtracking(perm, visited):
            if len(perm)==n:
                ans.append(perm[:])
                return 

            for i in range(n):
                curr = nums[i]
                if visited[i] == False:
                    perm.append(curr)
                    visited[i] = True
                    backtracking(perm, visited)
                    perm.pop()
                    visited[i] = False
            
        backtracking([],[False]*len(nums))
        return ans