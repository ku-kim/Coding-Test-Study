"""
	문제    : 스타트와링크
    유형    : 완전탐색
	난이도  : 하
	시간    : 5m
	uri    : https://www.acmicpc.net/problem/14889
    날짜    : 1x(21.7.1)
"""
import itertools

n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
people = [i for i in range(n)]
teams = set(itertools.combinations(people,n//2))

result = []
for team_A in teams:
    start_team = link_team = 0

    for x in team_A:
        for y in team_A:
            start_team += maps[x][y]
    
    team_B = [i for i in range(n) if i not in team_A]
    for x in team_B:
        for y in team_B:
            link_team += maps[x][y]

    result.append(abs(start_team - link_team))

print(min(result))