import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    
    for op in operations:
        ins, val = op.split()
        val = int(val)
        if ins == 'I':
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
        elif ins == 'D' and val == -1 and min_heap:
            sync_val = heapq.heappop(min_heap)
            max_heap.remove(-sync_val)
        elif ins == 'D' and val == 1 and max_heap:
            sync_val = heapq.heappop(max_heap)
            min_heap.remove(-sync_val)
    
    if min_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]
