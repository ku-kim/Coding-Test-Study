from typing import List

import collections
def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)
    days = 1
    counts = []

    count = 0
    while progresses:
        if progresses[0] + days*speeds[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        else:
            if count > 0:
                counts.append(count)
                count = 0
            days += 1
    counts.append(count)
    return counts

progresses = [93, 30, 55]	
speeds = [1, 30, 5]	
print(solution(progresses, speeds))