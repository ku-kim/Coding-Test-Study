"""
	문제    : 동전1
    유형    : DP
	난이도  : 44%, lv2
	시간    : 10m 
	uri    : https://www.acmicpc.net/problem/2293
"""

#   1 2 3 4 5 6 7 8 9 10
# 1
# 2
# 5
# s
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)

dp[0] = 1

for i in coins:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[k])
