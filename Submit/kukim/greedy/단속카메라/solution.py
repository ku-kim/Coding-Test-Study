"""
	문제    : 단속카메라
    유형    : 그리디
	난이도  : lv3
	시간    : 30m
	uri    : https://programmers.co.kr/learn/courses/30/lessons/42884
    날짜    : 1x(21.10.16)
"""
from typing import List
import sys
# Big-O : O(n)
def solution(routes: List[List[int]]) -> int:
    routes.sort(key = lambda x: x[1])
    camera_pos = -sys.maxsize
    count = 0

    for route in routes:
        if camera_pos < route[0]:
            count += 1
            camera_pos = route[1]
    return count

#### input & output
# Input: 
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	
# Output: 2

print(solution(routes))