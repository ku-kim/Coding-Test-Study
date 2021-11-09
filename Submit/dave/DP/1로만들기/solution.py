"""
정수 X (1 <= X <= 10^6)

연산 3가지
    - X가 3으로 나눠 떨어지면 3으로 나눈다.
    - X가 2로 나눠 떨어지면 2로 나눈다.
    - 1을 뺀다.


X = 1 이면 1을 뺀다.     (0회)
X = 2 이면 2로 나눈다.    (1회)
X = 3 이면 3으로 나눈다.   (1회)
X = 4 이면
    1을 빼고 3으로 나눈다.  (2회)
    2로 나누고 2로 나눈다.  (2회)
X = 5 이면
    1을 빼고 X = 4 일 때의 최저 횟수를 더한다. (3회)
X = 6 이면
    1을 빼고 X = 5 일 때의 최저 횟수를 더한다. (4회)
    2로 나눈 값이 3이므로 op_count(3) + 1   (2회)
    3으로 나눈 값이 2이므로 op_count(2) + 1 (2회)

X가 2 또는 3으로 나눠지지 않을 때는 op_count(X - 1) + 1


    if X == 1 then 0
    if X == 2 then 1
    if X == 3 then 1
    if X > 3 then
        1. op_count(X - 1)
        2. if X % 2:
            op_count(X/2)
        3. if X % 3:
            op_count(X/3)
        X = min(1, 2, 3) + 1
"""
X = int(input())
INF = int(1e9)

dp = [INF] * (X + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, X + 1):
    if i % 2 == 0 and i % 3 != 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    elif i % 2 != 0 and i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    elif i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i // 2], dp[i // 3], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp[X])

