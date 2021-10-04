"""
	문제    : 사칙연산
    유형    : DP
	난이도  : 상 lv4
	시간    : 
	uri    : https://programmers.co.kr/learn/courses/30/lessons/1843
    날짜    : 1x(21.9.1)
"""

def solution(arr):
    length = (len(arr) + 1) // 2
    # print(length)
    dp_max = [[-1000000 for _ in range(101)] for _ in range(101)]
    dp_min = [[1000000 for _ in range(101)] for _ in range(101)]
    
    for i in range(0, len(arr), 2):
        dp_max[i // 2][i // 2] = arr[i]
        dp_min[i // 2][i // 2] = arr[i]

arr = ["1", "-", "3", "+", "5", "-", "8"] # 1
# arr = ["5", "-", "3", "+", "1", "+s", "2", "-", "4"]  # 3		
print(solution(arr))