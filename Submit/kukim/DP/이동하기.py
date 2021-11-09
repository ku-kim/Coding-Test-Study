"""
	문제    : 이동하기
    유형    : DP
	난이도  : 57%, lv1~2
	시간    : 10m 
	uri    : https://www.acmicpc.net/problem/11048
"""

# 오른쪽, 아래, 아래 대각선 이동만 가능

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]


dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1],
                       dp[i-1][j-1]) + maps[i - 1][j - 1]
print(dp[n][m])
