from heapq import heappush, heappop

def solution(jobs):
    ## 목표: 작업이 걸리는 최소 평균 시간을 구해서 리턴
    ## 1. jobs를 요청시간을 기준으로 정렬
    ## 2. 원소의 요청시간이 end보다 작은것들 전부 heap에 (need, time)로 삽입
    ## 3. heap에 원소가 있으면
        ## 3-1. need, time = heappop(heap)
        ## 3-2. end += need
        ## 3-3. tot += end - time
    ## 4. 없으면, end += 1
    ## 5. jobs의 원소가 전부 사라질때까지 2-5번 반복
    ## 6. return tot / len(jobs)
    
    jobs.sort()
    end = tot = i = 0
    start = -1
    heap = []
    
    while len(jobs) > i:
        for time, need in jobs:
            if start < time <= end:
                heappush(heap, [need, time])

        if heap:
            need, time = heappop(heap)
            start = end
            end += need
            tot += end - time
            i += 1
        else:
            end += 1
            
    return tot // len(jobs)