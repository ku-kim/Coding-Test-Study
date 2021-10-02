from heapq import heapify, heappush, heappop

def change_heap(arr):
    h = list(map(lambda x: -x, arr))
    heapify(h)
    return h

def solution(operations):
    minheap = []
    maxheap = []
    
    for op in operations:
        command, num = op.split()
        
        if command == "I":
            heappush(minheap, int(num))
            heappush(maxheap, -int(num))
        elif maxheap and command == "D" and num == "1":
            heappop(maxheap)
            minheap = change_heap(maxheap)
        elif minheap and command == "D" and num == "-1":
            heappop(minheap)
            maxheap = change_heap(minheap)
            
    if minheap:
        return [max(minheap), min(minheap)]
    
    return [0, 0]