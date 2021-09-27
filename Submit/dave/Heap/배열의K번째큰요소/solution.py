class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use max heap
        nums_heap = list()
        for num in nums:
            heapq.heappush(nums_heap, -num)
        
        k_th_largest = int()
        for _ in range(k):
            k_th_largest = heapq.heappop(nums_heap)
        
        return -k_th_largest
