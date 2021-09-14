from collections import deque

def solution(priorities, location):
    ## 목적 : 원하는 위치의 것을 출력해내는데까지 걸리는 시간 구하기
    priorities = deque([(idx, p) for idx, p in enumerate(priorities)])
    count = 0
    while priorities:
        _, most_prior = max(priorities, key=lambda x: x[1])
        idx, prior = priorities.popleft()
        
        if prior >= most_prior:
            count += 1
            if idx == location:
                return count
        else:
            priorities.append((idx, prior))