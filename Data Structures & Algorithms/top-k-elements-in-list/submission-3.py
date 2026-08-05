class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # occurances = {}

        # occurances = dict(sorted(occurances.items(), key=lambda item: item[1]))
        # #print(occurances)
        # return(list(occurances.keys())[len(occurances)-k:])

        counts_of_each = {}    

        freq = [[] for i in range(len(nums)+1)]
        #.get(i,0)
        for i in nums:
            if i in counts_of_each:
                counts_of_each[i] += 1
            else:
                counts_of_each[i] = 1

        for n,c in counts_of_each.items():
            #print (c)
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) ==k:return res

