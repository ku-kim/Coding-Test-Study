"""
n = 동전 종류        (1 <= n <= 100)
k = 만들어야 할 액수   (1 <= k <= 10,000)

1, 5, 12를 적절히 조합하여 15를 만들 수 있는 최소 동전 수량.
14를 만드는데 드는 최소 동전 수 + 1
    13을 만드는데 드는 최소 동전 수 + 1
        12를 만드는데 드는 최소 동전 수 + 1
        8을 만드는데 드는 최소 동전 수 + 1
        1을 만드는데 드는 최소 동전 수 + 1
    9를 만드는데 드는 최소 동전 수 + 1
    2를 만드는데 드는 최소 동전 수 + 1
10을 만드는데 드는 최소 동전 수 + 1
    9를 만드는데 드는 최소 동전 수 + 1
    5를 만드는데 드는 최소 동전 수 + 1
3을 만드는데 드는 최소 동전 수 + 1
    2를 만드는데 드는 최소 동전 수 + 1
        1을 만드는데 드는 최소 동전 수 + 1

dp table 초기화
dp = [INF] * (k + 1)
dp[0] = 0

점화식: min(dp[index], dp[index - coin_value] + 1)
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
0 1 2 3 4 1 2 3 4 5  2  3  1  2  3  3
"""
n, k = map(int, input().split())
coins = list()
for _ in range(n):
    coins.append(int(input()))

INF = int(1e9)
dp = [INF] * (k + 1)
dp[0] = 0

for coin in coins:
    for price in range(coin, k + 1):
        if dp[price] > dp[price - coin] + 1:
            dp[price] = dp[price - coin] + 1

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])

