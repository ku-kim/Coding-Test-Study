"""
동전 종류별로 조합하여 k원을 만들 수 있는 모든 경우의 수
    -동전은 몇개를 사용하더라도 상관없다.
    -동전의 순서가 바뀌더라도 하나의 경우의 수로 친다.
     예를 들어 1,2,2와 2,2,1은 동일한 경우이다.

풀이를 위한 아이디어.
가액이 X원인 동전을 더해서 금액 T를 만들 수 있는 경우의 수 = 각 동전을 사용해 금액 (T - X)를 만들 수 있는 모든 경우의 수
따라서 모든 동전에 대해 위의 과정을 거친 후 마지막 계산 된 값이 k원을 만들 수 있는 모든 경우의 수가 된다.

위의 내용에 따라 다음과 같이 DP 테이블을 작성해갈 수 있다.

    1 2 3 4 5 6 7 8 9 10
1   1 1 1 1 1 1 1 1 1  1
2   0 1 1 2 2 3 3 4 4  5
5   0 0 0 0 1 1 2 2 3  4
T   1 2 2 3 4 5 6 7 8 10
"""

n, k = map(int, input().split())
coins = list()
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k + 1)
for coin in coins:
    for price in range(coin, k + 1):
        if price == coin:
            dp[price] += 1
        else:
            pre_price = price - coin
            dp[price] += dp[pre_price]

print(dp[-1])

