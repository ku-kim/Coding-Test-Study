"""
	문제    : 좋은수열 
    유형    : 완전탐색, 백트랙킹
	난이도  : 중
	시간    : 30m
	uri    : https://www.acmicpc.net/problem/2661
    날짜    : 1x(21.10.6)
"""

'''
    - case 1
        - n 길이까지 경우의 수 모두 체크
            - 최대 경우의 수가 3^80 이라서 불가능
    - case 2
        dfs : 하나씩 탐색하면서 유효성 검사
'''

def invaild_seq(idx):
    for i in range(1, (idx // 2) + 1):
        if s[-i:] == s[-2*i:-i]:
            return True

def dfs(idx):
    if invaild_seq(idx):
        return -1

    if idx == n:
        print("".join(s))
        return 0
    
    for i in "123":
        s.append(str(i))
        if dfs(idx + 1) == 0:
            return 0
        s.pop()

n = int(input())
s = []
dfs(0)