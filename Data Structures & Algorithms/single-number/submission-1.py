class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # we can do stack and add /remove with for loop

        res = 0
        for i in nums:
            #XOR operator
            res = res ^ i

        return res