from typing import List
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    return sorted(points, key = lambda x : x[0] ** 2 + x[1] ** 2)[:k]

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))