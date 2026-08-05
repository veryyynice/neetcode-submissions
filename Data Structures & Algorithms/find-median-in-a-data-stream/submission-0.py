class MedianFinder:
    #9,4   2,3
    #BY DEFAULT PYTHON HAS MIN HEAP
    #keep adding to each heap
    #if there is tie just add to small Heap if number is less than top of largeHeap 
    
    #for findMedian  we return from bigger of the heaps 

    def __init__(self):
        self.smallHeap = [] #max heap
        self.largeHeap = [] #min heap
    #1 2     3 , and we get 4. 
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap,-num)

        largest_in_small = -heapq.heappop(self.smallHeap)
        heapq.heappush(self.largeHeap, largest_in_small)

        if len(self.largeHeap) > len(self.smallHeap):
                    smallest_in_large = heapq.heappop(self.largeHeap)
                    heapq.heappush(self.smallHeap, -smallest_in_large)

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.largeHeap):
            return (float(-self.smallHeap[0])+self.largeHeap[0])/2
        elif len(self.smallHeap)> len(self.largeHeap):
            return -(self.smallHeap[0])
        #should never be:
        else:
            return (self.largeHeap[0])

        
        