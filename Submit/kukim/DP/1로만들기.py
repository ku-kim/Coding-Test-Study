"""
	문제    : 1로 만들기
    유형    : DP
	난이도  : 31%, lv3
	시간    : 10m 
	uri    : https://www.acmicpc.net/problem/1463
"""


def solution(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
    return dp[n]


#n = int(input())
#dp = [0] * (n + 1)
# for i in range(2, n + 1):
#    dp[i] = dp[i - 1] + 1

#    if i % 3 == 0:
#        dp[i] = min(dp[i], dp[i // 3] + 1)
#    if i % 2 == 0:
#        dp[i] = min(dp[i], dp[i // 2] + 1)
# print(dp[n])

n = 2  # 1
n = 10  # 3
print(solution(n))
