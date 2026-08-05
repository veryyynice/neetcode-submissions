class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visited = {}
        for i in range(len(nums)):
            current = nums[i]
            if (target-current) in visited:
                return [visited[(target-current)],i]
            visited[current] = i                

#1,0,2,3 target was 5
