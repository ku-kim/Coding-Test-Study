"""
	문제    : 기지국 설치
    유형    : 인덱싱, 투포인터, 구현
	난이도  : 하
	시간    : 10m
	uri    : https://programmers.co.kr/learn/courses/30/lessons/12979?language=python3
"""

'''
    왼쪽부터 조건에 맞는지 체크
    O(n)
'''
def solution(n, stations, w):
    i = 0
    left = 1

    answer = 0
    while left <= n:
        if i < len(stations) and left >= stations[i] - w:
            left = stations[i] + w + 1
            i += 1
        else:
            left += (2 * w) + 1
            answer += 1
    return answer


n = 11
stations = [4, 11]
W = 1

print(solution(n, stations, W))