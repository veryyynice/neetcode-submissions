
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #sqrt((x1 - x2)^2 + (y1 - y2)^2))
        #min heap but also IMPROVED is max heap

        #min heap
        res = []
        minHeap = []
        for point in points:
            x,y = point[0],point[1]
            distance = math.sqrt((x**2)+(y**2))
            minHeap.append([distance,x,y])

        heapq.heapify(minHeap)

        while k>0:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        
        return res


