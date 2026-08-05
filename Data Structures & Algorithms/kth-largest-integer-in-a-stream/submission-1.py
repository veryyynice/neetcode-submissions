class KthLargest:
    #kth largest int in nums
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        while (len(self.minHeap)>k):
            heapq.heappop(self.minHeap)

        # self.arr = nums
        # self.k = k
    def add(self, val: int) -> int:
        # self.arr.append(val)
        # self.arr = sorted(self.arr)
        # return(self.arr[-self.k])
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]