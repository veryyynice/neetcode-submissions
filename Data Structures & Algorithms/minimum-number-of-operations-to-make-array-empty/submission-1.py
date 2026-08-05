class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #positive
        #one operation is remove 2 dupicates
        #one operation is remove 3 duplicates
        #return min num of opeartions
        #or -1 is not possible

        #if there is unique val return -1

        #dp max of 

        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num,0)+1

        #fibonacci min(count(4-2),(4-3)) is dp

        #greedy(diving)
        res = 0

        for n,c in frequencies.items():
            if c==1:
                return -1
            res += math.ceil(c/3)

        return res