from typing import List
from collections import deque

def solution(priorities: List[int], location: int):
    answer = 0
    queue = deque([v,k] for k,v in enumerate(priorities))
    
    while queue:
        item = queue.popleft()
        if item[0] < max(queue)[0]:
            queue.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

priorities = [2, 1, 3, 2]	
location = 2
print(solution(priorities, location))
