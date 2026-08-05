class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            curr = nums[i]
            if (target - curr) in dictionary and dictionary[(target-curr)] != i:
                return ([dictionary[target-curr],i])
            dictionary[nums[i]] = i
        
        return []