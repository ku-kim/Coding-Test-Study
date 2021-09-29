    def findKthLargest(nums, k):
        return sorted(nums, reverse=True)[k-1]