"""
	문제    : 회의실 배정
    유형    : 구현 
	난이도  : 하
	시간    : 20m
"""

'''
    - 정렬
        회의 끝나는시간 -> 회의 시작시간 기준 정렬 (시작시간 기준 정렬하면 [[2, 4], [2, 2],[1,20000]] 잡지못함)
    - 다음 팀의 회의의 시작 시간이 이전 회의실에 들어있는 팀의 끝나는 시간보다 크면, 회의 가능
    Big-O : O(n)\
'''

def solution(arr):
    arr.sort(key = lambda x: (x[1], x[0]))
    
    time = 0
    answer = 0
    for team in arr:
        if team[0] >= time:
            time = team[1]
            answer += 1
    return answer


arr = [[1, 2], [2, 4], [2, 2]]	# 3
arr = [[1, 2], [2, 4], [2, 2],[1,20000]]	# 3
# arr = [[2, 4], [2, 2],[1,20000]]	# 2
# arr = [[1, 4], [2, 6], [4, 7]]	# 2

print(solution(arr))