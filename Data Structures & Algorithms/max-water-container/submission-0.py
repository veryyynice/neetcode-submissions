class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #l and right pointers 
        #get highest pointers
        l, r = 0, len(heights)-1
        result = 0
        result = min(heights[r],heights[l])*(r-l)
        #area between two pointers is smaller pointer  height * (r-l)
        while l < r:
            new_area = min(heights[r],heights[l])*(r-l)
            if (new_area) > result:
                result = new_area
            #we move smaller 
            
            if (heights[l] < heights[r]):
                l+=1
            else: r-=1
        return result
            