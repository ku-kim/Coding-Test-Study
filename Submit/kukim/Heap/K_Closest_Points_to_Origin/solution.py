from typing import List
import heapq

# heap
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for x, y in points:
        heapq.heappush(heap, ((x ** 2 + y ** 2), [x,y]))
    
    return [heapq.heappop(heap)[1] for _ in range(k)]

# list sorting
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    return sorted(points, key = lambda x : x[0] ** 2 + x[1] ** 2)[:k]


points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))