class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #return minimum eating rate so that piles gets eaten within h hours
        #start from k =1

        max_piles = max(piles)
        if h==len(piles):
            return max_piles

        #upper limit for answer is h
        #brute force is check from 1 to upper limit (max elemtn)
        #binary seach from lower limit for upper limit
        res = max_piles
        l,r = 1,max_piles

        while l<=r:
            #k
            mid = (l+r)//2

            curr_hours = 0
            for pile in piles:
                curr_hours += math.ceil(float(pile)/mid)
            if curr_hours<=h:
                res= mid
                r = mid-1
                
            else:
                l=mid+1

        return(res)
