"""
	문제    : 위장
    유형    : 해쉬
	난이도  : 중 lv2
	시간    : 20m
	uri    : https://programmers.co.kr/learn/courses/30/lessons/42578
"""

from collections import defaultdict
def solution(clothes):
    clothes_cases = defaultdict(list)

    answer = 1
    for case in clothes:
        clothes_cases[case[1]].append(case[0])
    for case in clothes_cases.values():
        answer *= (len(case) + 1)
    answer -= 1
    return answer
