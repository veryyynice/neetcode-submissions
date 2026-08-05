class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = {}
        for i in nums:
            if i in occurances:
                occurances[i] += 1
            else:
                occurances[i] = 1
        occurances = dict(sorted(occurances.items(), key=lambda item: item[1]))
        print(occurances)
        return(list(occurances.keys())[len(occurances)-k:])