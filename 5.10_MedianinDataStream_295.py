class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self.large_heap = []
        self.small_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large_heap, num)
        
        large_top = heapq.heappop(self.large_heap)
        
        heapq.heappush(self.small_heap, -1 * large_top)

        if len(self.small_heap) > len(self.large_heap):
            heapq.heappush(self.large_heap, -1 * heapq.heappop(self.small_heap))

    def findMedian(self) -> float:
        if len(self.large_heap) == len(self.small_heap):
            return (self.large_heap[0] + (-1 * self.small_heap[0])) / 2
        else:
            return self.large_heap[0]