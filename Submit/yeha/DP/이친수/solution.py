def solution():
    n = int(input())
    answer = [1] * n
    for i in range(2, n):
        answer[i] = answer[i - 1] + answer[i - 2]
    print(answer[n - 1])