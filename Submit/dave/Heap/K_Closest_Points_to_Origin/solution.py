import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # data that is inserted in heap is like "(distance, [x, y])"
        heap = list()
        for p in points:
            heapq.heappush(heap, (p[0] ** 2 + p[1] ** 2, p))

        result = list()
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
