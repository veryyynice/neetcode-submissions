class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #negate for max heap
        stones = [-s for s in stones]
        #make stones into min heap
        heapq.heapify(stones)

        while len(stones) >1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            #second is smaller:
            if second > first:
                #by subtracting we make it bigger , so less prio and depth in min heap
                heapq.heappush(stones,first-second)
            #if empty it would return 0 if not it would return the remainer stone
        stones.append(0)
        #return most prio from min heap
        return(abs(stones[0]))