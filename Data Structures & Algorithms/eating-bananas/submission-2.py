class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #needs to be <= h
        #k=1
        #piles.sort()
        #maximum = max(piles)
        #k <= maximum:
        l, r= 1, max(piles)
        res = r
        while (l<=r):
            #print(l,r)
            mid = (r+l)//2
            #temp_piles = piles
            temp_hours = 0
            #print(mid)
            for pile in piles:
                #if temp_hours > h: break
                hours_needed = int(math.ceil(pile/mid))
                temp_hours += hours_needed
            #what to about= 
            #
            if temp_hours <=h:
                res = min(res,mid)
                r = mid-1
            elif temp_hours > h:
                l = mid+1

        return res        



