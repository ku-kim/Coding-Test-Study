"""
	문제    : 땅따먹기
    유형    : 그리디
	난이도  : 중
	시간    : 
	uri    : https://programmers.co.kr/learn/courses/30/lessons/12913
    날짜    : 1x(21.6.30)
"""

def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[len(land)-1])


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]	

print(solution(land))