"""
문제    : 동전2
유형    : DP
난이도  : 44%, lv2
시간    : 10m
uri    : https://www.acmicpc.net/problem/2294
"""

# refer : https://pacific-ocean.tistory.com/203
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [10001] * (k + 1)
dp[0] = 0

for i in range(n):
    for j in range(coins[i], k+1):
        print(i, j)
        dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[-1] != 10001:
    print(dp[-1])
else:
    print('-1')
