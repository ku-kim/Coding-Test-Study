from heapq import heappush, heappop

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    answer = []
    heap = []
    for p in points:
        heappush(heap, ((p[0] ** 2 + p[1] ** 2) ** (1/2), p))
    
    while k:
        answer.append(heappop(heap)[1])
        k -= 1
    return answer