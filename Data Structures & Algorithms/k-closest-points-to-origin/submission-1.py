
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #sqrt((x1 - x2)^2 + (y1 - y2)^2))
        #min heap but also IMPROVED is max heap
        res = []
        maxHeap = []
        for point in points:
            x,y = point[0],point[1]
            distance = -math.sqrt((x**2)+(y**2))
            heapq.heappush(maxHeap,[distance,x,y])
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)

        while k>0:
            dist,x,y = heapq.heappop(maxHeap)
            res.append([x,y])
            k-=1
        
        return res


