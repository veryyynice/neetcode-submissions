class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #brute force with nested for loop checking if we got a decrease or increase or equal value
        ans = 0 #max area
        curr_min = 0
        for i in range(0,len(heights)):
            curr = heights[i]
            curr_min = curr
            if curr> ans:
                ans = curr
            if i == len(heights)-1:
                break
            else:
                for j in range(i+1,len(heights)):
                    nxt = heights[j]
                    curr_min = min(nxt,curr_min)
                    ans = max(ans, curr_min * (j+1-i))


        return ans