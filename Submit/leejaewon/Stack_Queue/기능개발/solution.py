from math import ceil
from collections import deque

def solution(progresses, speeds):
    ## 1. 배포에 걸리는 시간을 계산
    ## 2. 빈 배열에 deploy를 하나씩 옮김
    ## 3. 현재 값 보다 크면 여태 모아 놓은 deploy 값들을 answer로 옮기고, 비우기
    ## 4. 작으면 빈 배열에 계속 keep
    answer = []
    deploy = deque([ceil((100 - p) / s) for p, s in zip(progresses, speeds)])
    count = 1
    max_date = deploy.popleft()
    
    while deploy:
        d = deploy.popleft()
        
        if max_date < d:
            answer.append(count)
            max_date = d
            count = 1
        else:
            count += 1
            
    answer.append(count)
    return answer