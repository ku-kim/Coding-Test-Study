"""
	문제    : 이친수
    유형    : DP
	난이도  : 38%, lv2
	시간    : 10m
	uri    : https://www.acmicpc.net/problem/2193
"""

n = int(input())

dp = [1] * (n + 1)

if n >= 3:
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n - 1])
