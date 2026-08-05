class Solution:
    def trap(self, height: List[int]) -> int:
        #2 pointers
        #precompute and store in arrays
        n = len(height)
        prefix = [0]*n
        suffix = [0]*n

        for i in range(1,n):
            # if i == 0:
            #     prefix[i] = 0
            #     continue
            if height[i-1] > prefix[i-1]:
                prefix[i] = height[i-1]
            else:
                prefix[i] = prefix[i-1]
        
        for i in range(n-2,-1,-1):
            # if i == (n-1):
            #     suffix[i] = 0
            #     continue
            if height[i+1] > suffix[i+1]:
                suffix[i] = height[i+1]
            else:
                suffix[i] = suffix[i+1]

        res = [0]*n
        for i in range(n):
            water = min(suffix[i],prefix[i]) -height[i]
            if water >= 0:
                res[i] = water
        print(res)
        print(prefix)
        print(suffix)
        return sum(res)