class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        #same as choose (1)
        #n is the max value
        #k is the size of subarray

        #backtrack
        def recursion(i, arr):
            if i > n:
                if len(arr) == k:
                    res.append(arr.copy())
                return
            
            arr.append(i)
            recursion(i+1, arr)
            arr.pop()
            recursion(i+1,arr)
        recursion(1,[])
        return res

