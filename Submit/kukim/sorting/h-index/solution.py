"""
	문제    : h-index
    유형    : 정렬 
	난이도  : 하, lv2
	시간    : 30m
	uri    : https://programmers.co.kr/learn/courses/30/lessons/42747
    날짜    : 1^(21.10.10)
"""
from typing import List

'''
    1. 정렬
    2. h-index 계산, 현재 논문 인용수가 남은 개수보다 크거나 같을 때 
    3. 리턴
    
    
    0 1 3 5 6
    0 >= 4
      1 >= 4
        3 >= 3
        
0, 6

'''
def solution(citations):
    citations.sort()
    number_of_papers = len(citations)
    for i, citation in enumerate(citations):
        if citation >= number_of_papers - i:
            #print(citation, i, number_of_papers)
            return number_of_papers - i
    return 0

citations = [3, 0, 6, 1, 5]	
print(solution(citations)) # 3