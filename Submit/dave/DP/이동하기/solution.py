"""
(n, m) 위치에서의 최대 사탕 개수는
    (n-1, m), (n, m-1), (n-1, m-1) 위치의 사탕 개수 + (n, m) 사탕개수 중 최대값이다.
map[n][m] = max(map[n-1][m], map[n][m-1], map[n-1][m-1]) + map[n][m]
"""
import sys
f_input = sys.stdin.readline

N, M = map(int, f_input().split())

dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j, v in enumerate(map(int, f_input().split()), 1):
        dp[i][j] = v

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + dp[i][j]

print(dp[N][M])

