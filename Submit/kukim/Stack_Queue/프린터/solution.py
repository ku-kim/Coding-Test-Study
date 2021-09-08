from typing import List
#from collections import deque

def solution(priorities: List[int], location: int):
    queue = [[k, v] for k,v in enumerate(priorities)]
    answer = []
    while queue:
        if queue[0][1] == max(queue, key = lambda x: x[1])[1]:
            answer.append(queue.pop(0))
        else:
            queue.append(queue.pop(0))
    for i, values in enumerate(answer):
        if values[0] == location + 1:
            return i
    # 미완성
priorities = [2, 1, 3, 2]	
location = 2
print(solution(priorities, location))