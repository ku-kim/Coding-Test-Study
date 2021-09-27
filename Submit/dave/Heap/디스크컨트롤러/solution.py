import heapq
from collections import deque


def solution(jobs):
    jobs_q = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    heap = []
    heapq.heappush(heap, jobs_q.popleft())
    e_time = 0
    total_time = 0

    while heap:
        job_inf = heapq.heappop(heap)
        p_time = job_inf[0]
        r_time = job_inf[1]
        e_time = max(e_time + p_time, r_time + p_time)
        total_time += e_time - r_time
        while len(jobs_q) > 0 and jobs_q[0][1] <= e_time:
            heapq.heappush(heap, jobs_q.popleft())
        if len(jobs_q) > 0 and len(heap) == 0:
            heapq.heappush(heap, jobs_q.popleft())

    return total_time // len(jobs)

