    """
        문제    : 병합정렬
        유형    : 정렬
        난이도  : 중, medium
        시간    : 20m
        uri    : https://leetcode.com/problems/merge-intervals/submissions/
        날짜    : 1o(21.10.10)
    """
from typing import List

'''
    1. start -> end 순 정렬
    2. start 와 다음 end 가 동일한지 체크 후 머지
'''

# case 1
from typing import List
from collections import deque
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda x : (x[0], x[1]))
    intervals = deque(intervals)

    left = 0
    answer = []
    for i in range(len(intervals) - 1):
        #print(i, left, intervals)
        if intervals[left][1] >= intervals[left + 1][0]:
            # print(i, left, intervals, intervals[left][1] , intervals[left + 1][0])
            left_value = intervals.popleft()
            right_value = intervals.popleft()
            if left_value[1] >= right_value[1]:
                intervals.appendleft(left_value)
            else:
                # print("what", intervals)
                intervals.appendleft([left_value[0], right_value[1]])
                # print("what", intervals)
        else:
            answer.append(intervals.popleft())
    if intervals:
        answer.append(intervals.pop())
    return answer


# case 2 : soultion
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda i: i[0])
    res = [intervals[0]]
    for start, end in intervals[1:]:
        lastend = res[-1][1]
        if start<=lastend:
            res[-1][1] = max(lastend, end)
            
        else:
            res.append([start, end])

    
    return res
#Input: 
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


print(merge(intervals))