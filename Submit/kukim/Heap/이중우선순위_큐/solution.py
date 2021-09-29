from typing import List
import heapq

def solution(operations: List[str]) -> List[int]:
    min_heap = []
    max_heap = []
    
    for operation in operations:
        cmd, val = operation.split()
        val = int(val)
        
        if cmd == 'I':
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
        elif cmd == 'D':
            if not min_heap:
                continue
            if val == 1:
                max_val = heapq.heappop(max_heap)
                min_heap.remove(-max_val)
            elif val == -1:
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-min_val)
    if min_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]
        
operations = ["I 16","D 1"]	
print(solution(operations))