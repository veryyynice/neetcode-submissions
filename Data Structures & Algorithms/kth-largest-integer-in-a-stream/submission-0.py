class KthLargest:
    #kth largest int in nums
    def __init__(self, k: int, nums: List[int]):
        # self.minHeap, self.k = nums, k
        # heapq.heapify(self.minHeap)
        self.arr = nums
        self.k = k
    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr = sorted(self.arr)
        return(self.arr[-self.k])